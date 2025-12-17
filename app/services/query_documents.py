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
    Identify and extract relevant content from a collection of documents based on a given query.

    This function performs the following steps:
    1. Evaluates the relevance of each document to the provided query using an LLM (Large Language Model).
    2. Selects the most relevant document(s).
    3. Extracts specific nodes or segments from the selected document(s) that are most pertinent to the query.

    Args:
        query (str): The user query or search term to evaluate against the documents.
        documents (List[str]): A list of document contents as strings.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries where each dictionary contains:
            - "document": The original document text or identifier.
            - "relevance_score": A numeric score indicating how relevant the document is to the query.
            - "relevant_nodes": A list of extracted text segments or nodes that match the query context.
    """

    logger.info("Call to handle_query_documents with arguments query=%s and documents=%s", query, documents)

    # 1. Step: get trees according to documents and query TODO into seperate function?
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
    
    if len(tree_list) == 1:
        tree_path = tree_list[0]

    if len(tree_list) > 1:
        logger.info("Start Document selection process.")
        document_descriptions = []
        for tree_path in tree_list:
            try:
                with open(tree_path, "r", encoding="utf-8") as f:
                    tree = json.load(f)
            except FileNotFoundError:
                logger.exception("Error: File not found.")
            except json.JSONDecodeError as e:
                logger.exception("Error doecing JSON")
            except Exception as e:
                logger.exception("Unexpected error")
            doc_dict = {"doc_name": tree["doc_name"], "doc_path": tree_path, "doc_description": tree["doc_description"]}
            document_descriptions.append(doc_dict)

        doc_search_prompt = f""" 
            You are given a list of documents with their file names, and descriptions. Your task is to select one document that may contain information relevant to answering the user query.
            
            Query: {query}
            
            Documents: {document_descriptions}
            
            Response Format:
            {{
                "thinking": "<Your reasoning for document selection>",
                "answer": <Python list of relevant doc_path>, e.g. ['data/MIL-STD-111.pdf']. Return [] if no document is relevant.
            }}
            
            Return only the JSON structure, with no additional output.
            """
        logger.debug("Prompt to seach for nodes: %r", doc_search_prompt)

        llm = LLMClient()

        messages = []  #
        messages.append({"role": "user", "content": doc_search_prompt})

        logger.info("Llm will be called with %s", doc_search_prompt[:100])
        doc_search_result = llm.generate(messages)
        logger.info("llm returned %s", doc_search_result.content)

        # Answer from LLM contains backticks to indicate a JSON file
        llm_answer = doc_search_result.content
        if llm_answer.startswith("```"): # will be replaced by structured output
            llm_answer = re.sub(r"^```(?:json)?\s*", "", llm_answer, flags=re.IGNORECASE).strip()
            llm_answer = re.sub(r"```$", "", llm_answer).strip()

        doc_search_result_json = json.loads(llm_answer)
        selected_document = doc_search_result_json["answer"]
        if len(selected_document) == 0:
            logger.info("llm did not find relevant documents with reasoning %s", doc_search_result_json["thinking"])
            return [{"document_name": "", "nodes": ""}]
        elif len(selected_document) == 1:
            tree_path = selected_document[0]
            logger.debug("llm returned %s with reasoning %s", selected_document, doc_search_result_json["thinking"])
        else:
            raise HTTPException(status_code=404, detail=f"Too many documents returned.")

    # 2. Step: remove text from nodes (see utils.remove_fields) TODO as method into tree class

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

    # 3. Step: select nodes TODO into seperate function?

    tree_search_prompt = f"""
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
    logger.debug("Prompt to seach for nodes: %r", tree_search_prompt)

    llm = LLMClient()

    messages = []  
    messages.append({"role": "user", "content": tree_search_prompt})

    logger.info("Llm will be called with %s", tree_search_prompt[:100])
    tree_search_result = llm.generate(messages)
    logger.info("llm returned %s", tree_search_result.content)

    # query LLM
    flattened_nodes = get_nodes(
        tree["structure"]
    )

    logger.debug("flattend nodes looks like %r", flattened_nodes)

    ## transform flattened nodes into node map TODO add to tree class
    node_map = {}
    for node in flattened_nodes:
        node_map[node["node_id"]] = {
            "title": node["title"],
            "start_index": node["start_index"],
            "end_index": node["end_index"],
            "node_id": node["node_id"],
            "text": node["text"],
            "summary": node["summary"],
        }
    logger.debug("node_map looks like %r", node_map)

    relevant_nodes = []

    # Answer from LLM contains backticks to indicate a JSON file
    llm_answer = tree_search_result.content 
    if llm_answer.startswith("```"): # will be replaced by structured output
        llm_answer = re.sub(r"^```(?:json)?\s*", "", llm_answer, flags=re.IGNORECASE).strip()
        llm_answer = re.sub(r"```$", "", llm_answer).strip()

    tree_search_result_json = json.loads(llm_answer)
    for node_id in tree_search_result_json["node_list"]:
        relevant_nodes.append(node_map[node_id])

    logger.info("Relevant nodes are: %s", relevant_nodes)

    # 4. return relevant nodes 
    return_value = [
        {"document_name": tree["doc_name"], "nodes": relevant_nodes}
    ]  # TODO: change documents[0] cause in any case only 1 Document will be returned

    return return_value
