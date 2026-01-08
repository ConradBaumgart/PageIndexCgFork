import json
from pathlib import Path
from typing import Any, Dict, List

from fastapi import HTTPException

from app.llm_client import LLMClient
from app.logging_config import get_logger
from pageindex.utils import get_json_content, get_nodes, remove_fields

logger = get_logger(__name__)

TREE_FOLDER = Path("app/data/generated_trees")


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
            - "relevant_nodes": A list of extracted text segments or nodes that match the query context.
    """

    logger.info("Call to handle_query_documents with arguments query=%s and documents=%s", query, documents)

    # 1. Step: get tree according to documents and query
    available_trees = list_available_trees(TREE_FOLDER)

    requested_trees = [
        tree for tree in available_trees if tree["doc_name"].lower() in [doc.lower() for doc in documents]
    ]

    logger.info("%d trees were found from %d documents requested.", len(requested_trees), len(documents))
    logger.debug("These documents were found when searching for trees: %r", requested_trees)

    selected_tree = select_relevant_tree(query=query, tree_list=requested_trees)

    # 2. Step: load tree and remove text from nodes

    try:
        tree = load_tree(selected_tree.get("doc_path"))
    except Exception as e:
        logger.exception("Unexpected error when loading tree.")
        raise HTTPException(status_code=500)

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
    logger.debug("Prompt to search for nodes: %r", tree_search_prompt)

    llm = LLMClient()

    messages = [{"role": "user", "content": tree_search_prompt}]

    tree_search_result = llm.generate(messages, json_response=True)

    # Clean LLM response from text which might spoil JSON strucutre
    llm_answer = get_json_content(tree_search_result.content)

    tree_search_result_json = json.loads(llm_answer)

    # create node_map to select nodes by node_id
    flattened_nodes = get_nodes(tree["structure"])
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
    for node_id in tree_search_result_json["node_list"]:
        relevant_nodes.append(node_map[node_id])

    logger.info("Relevant nodes are: %s", relevant_nodes)

    # 4. return relevant nodes
    return_value = [{"document_name": tree["doc_name"], "nodes": relevant_nodes}]

    return return_value


def list_available_trees(tree_folder: Path) -> List[dict[str, Any]]:
    """
    Lists all trees which are available in the tree location path.
    Args:
        tree_folder (Path): Path to folder where tree files are stored.
    Return:
        List[dict[str, Any]]: List of available trees containing name, description and path.
    """
    tree_list = []
    for json_path in tree_folder.rglob("*.json"):
        try:
            tree = load_tree(json_path)
        except (json.JSONDecodeError, OSError, FileNotFoundError):
            logger.warning("Skipping unreadable tree file: %s", json_path)
            continue
        doc_name = tree.get("doc_name")
        doc_description = tree.get("doc_description")
        tree_list.append({"doc_name": doc_name, "doc_description": doc_description, "doc_path": json_path})

    return tree_list


def load_tree(tree_path: Path) -> dict[str, Any]:
    """
    Loads a tree based on a Path and return the tree object.
    Args:
        tree_path (Path): path to tree JSON file.
    Return:
        dict[str, Any]: tree object
    """
    with tree_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def select_relevant_tree(query: str, tree_list: List[dict[str, Any]]) -> dict[str, Any]:
    """Select the most relevant document tree based on a query.

    If no trees are provided, raises an HTTP 404 error. If exactly one tree is provided,
    returns it directly. If multiple trees are provided, uses an LLM to select the most
    relevant one based on the query and document descriptions.

    Args:
        query (str): The user query to evaluate relevance against.
        tree_list (List[dict[str, Any]]): A list of document metadata dictionaries,
            containing 'doc_name', 'doc_description', and 'path'.

    Returns:
        dict[str, str]: The document metadata dictionary of the selected document tree.

    Raises:
        HTTPException: If no documents are found (404) or if selection fails (500).
    """

    if len(tree_list) == 0:
        raise HTTPException(status_code=404, detail=f"No documents were found.")

    if len(tree_list) == 1:
        return tree_list[0]

    logger.info("Start Document selection process.")

    doc_search_prompt = f""" 
        You are given a list of documents with their file names, and descriptions. Your task is to select one document that may contain information relevant to answering the user query.
        
        Query: {query}
        
        Documents: {tree_list}
        
        Response Format:
        {{
            "thinking": "<Your reasoning for document selection>",
            "answer": "<Python string of relevant doc_name>, e.g. 'MIL-STD-111.pdf'" 
        }}
        
        Return an empty string if no document is relevant.
        Return only the JSON structure, with no additional output.
        """
    logger.debug("Prompt to search for nodes: %r", doc_search_prompt)

    messages = [{"role": "user", "content": doc_search_prompt}]

    llm = LLMClient()
    llm_answer = llm.generate(messages, json_response=True)

    # Answer from LLM might contain backticks to indicate a JSON file
    doc_search_result = get_json_content(llm_answer.content)
    doc_search_result_dict = json.loads(doc_search_result)

    revelant_doc_name = doc_search_result_dict["answer"]

    if revelant_doc_name == "":
        logger.info("llm did not find relevant documents with reasoning %s", doc_search_result_dict["thinking"])
        return [{"document_name": "", "nodes": ""}]  # TODO might return 404 after clarification with Stephan

    relevant_tree = [document for document in tree_list if tree_list["doc_name"] == revelant_doc_name]

    if len(relevant_tree) != 1:
        raise HTTPException(status_code=500, detail=f"Document selection failed.")

    return relevant_tree[0]
