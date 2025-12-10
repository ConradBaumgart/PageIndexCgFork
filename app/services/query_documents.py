import json
import re
from pathlib import Path
from typing import Any, Dict, List

from fastapi import HTTPException

from app.llm_client import LLMClient
from app.logging_config import get_logger
from pageindex.utils import get_nodes, remove_fields

logger = get_logger(__name__)

RESULTS_DIR = Path("app/data/generated_trees")


def handle_query_documents(query: str, documents: List[str]) -> List[Dict[str, Any]]:
    """
    tbd
    """
    logger.info("Call to handle_query_documents with arguments query=%s and documents=%s", query, documents)

    # 1. Step: get trees according to documents
    tree_list = []
    for json_path in RESULTS_DIR.rglob("*.json"):
        try:
            with json_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            doc_name = data.get("doc_name")
            if doc_name in documents:
                tree_list.append(json_path)
        except (json.JSONDecodeError, OSError):
            logger.exception("Error when iterating through trees")
            continue

    logger.info("%d documents were found from %d documents requested.", len(tree_list), len(documents))
    logger.debug("These documents were found when searching for trees: %r", tree_list)

    if len(tree_list) == 0:
        raise HTTPException(status_code=404, detail=f"No documents were found.")

    # Current assumption: only one document is queried
    if len(tree_list) > 1:
        raise HTTPException(status_code=404, detail=f"Currently only 1 document can be queried.")
    tree_path = tree_list[0]  # change later!

    # 2. Step: remove text from nodes (see utils.remove_fields)

    try:
        with open(tree_path, "r", encoding="utf-8") as f:
            tree = json.load(f)
    except FileNotFoundError:
        logger.exception("Error: File not found.")
    except json.JSONDecodeError as e:
        logger.exception("Error doecing JSON")
    except Exception as e:
        logger.exception("Unexpected error")

    tree_without_text = remove_fields(tree, "text")
    logger.debug("Tree without text will be provided: %r", tree_without_text)

    # 3. Step: create prompt to select nodes

    search_prompt = f"""
    You are given a question and a tree structure of a document.
    Each node contains a node id, node title, and a corresponding summary.
    Your task is to find all nodes that are likely to contain the answer to the question.

    Question: {query}

    Document tree structure:
    {json.dumps(tree_without_text, indent=2)}

    Please reply in the following JSON format:
    {{
        "thinking": "<Your thinking process on which nodes are relevant to the question>",
        "node_list": ["node_id_1", "node_id_2", ..., "node_id_n"]
    }}
    Directly return the final JSON structure. Do not output anything else.
    """
    logger.debug("Prompt to seach for nodes: %r", search_prompt)

    # 4. Step: get LLM client
    llm = LLMClient()

    messages = []  #
    messages.append({"role": "user", "content": search_prompt})

    logger.info("Llm will be called with %s", search_prompt[:100])
    tree_search_result = llm.generate(messages)
    logger.info("llm returned %s", tree_search_result.content)

    # query LLM
    flattened_nodes = get_nodes(tree)

    logger.debug("flattend nodes looks like %r", flattened_nodes)

    ## transform flattened nodes into node map
    node_map = {}
    for node in flattened_nodes[0]["structure"]:
        node_map[node["node_id"]] = {
            "title": node["title"],
            "start_index": node["start_index"],
            "end_index": node["end_index"],
            "node_id": node["node_id"],
            "text": node["text"],
            "summarry": node["summary"],
        }
    logger.debug("node_map looks like %r", node_map)

    relevant_nodes = []

    # Answer from LLM contains backticks to indicate a JSON file
    llm_answer = tree_search_result.content
    if llm_answer.startswith("```"):
        llm_answer = re.sub(r"^```(?:json)?\s*", "", llm_answer, flags=re.IGNORECASE).strip()
        llm_answer = re.sub(r"```$", "", llm_answer).strip()

    tree_search_result_json = json.loads(llm_answer)
    for node_id in tree_search_result_json["node_list"]:
        relevant_nodes.append(node_map[node_id])

    logger.info("Relevant nodes are: %s", relevant_nodes)

    return_value = [
        {"document_name": documents[0], "nodes": relevant_nodes}
    ]  # TODO: change documents[0] cause in any case only 1 Document will be returned

    return return_value
