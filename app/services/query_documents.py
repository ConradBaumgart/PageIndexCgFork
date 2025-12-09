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
            continue

    logger.info(f"{len(tree_list)} documents where found from {len(documents)} documents requested.")

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
        print(f"Error: File '{tree_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    tree_without_text = remove_fields(tree, "text")
    logger.debug(f"Tree without text will be provided: {tree_without_text}")

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
    # 4. Step: get LLM client
    llm = LLMClient()

    messages = []  #
    messages.append({"role": "user", "content": search_prompt})

    tree_search_result = llm.generate(messages)
    logger.info(f"llm returned {tree_search_result.content}")

    # query LLM
    flattened_nodes = get_nodes(tree)
    logger.info(f"flattend nodes looks like {flattened_nodes}")

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
    logger.info(f"node_map looks like {node_map}")

    relevant_nodes = []

    llm_answer = tree_search_result.content

    if llm_answer.startswith("```"):
        llm_answer = re.sub(r"^```(?:json)?\s*", "", llm_answer, flags=re.IGNORECASE).strip()
        llm_answer = re.sub(r"```$", "", llm_answer).strip()

    tree_search_result_json = json.loads(llm_answer)
    for node_id in tree_search_result_json["node_list"]:
        relevant_nodes.append(node_map[node_id])
    logger.info(f"Relevant nodes are: {relevant_nodes}")

    return_value = [{"document_name": documents[0], "nodes": relevant_nodes}]

    return return_value
