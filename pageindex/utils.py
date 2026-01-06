import asyncio
import copy
import json
import logging
import os
import re
import time
from datetime import datetime
from io import BytesIO
from pathlib import Path
from types import SimpleNamespace as config
from typing import Any, Dict, List, Optional

import openai
import pymupdf
import PyPDF2
import tiktoken
import yaml
from dotenv import load_dotenv
from transformers import AutoTokenizer

from app.llm_client import LLMClient
from app.logging_config import get_logger

logger = get_logger(__name__)
load_dotenv()

MISTRAL_ENDPOINT = os.getenv("MISTRAL_ENDPOINT")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_MODEL = os.getenv("MISTRAL_MODEL")


def count_tokens_mistral(text: str) -> int:
    """
    Count tokens for a given text using Mistral's tokenizer.
    """

    # Load the tokenizer for Mistral (adjust model name if needed)
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-Large-Instruct-2411")

    if not text:
        return 0
    tokens = tokenizer.encode(text)
    return len(tokens)


def ChatGPT_API_with_finish_reason(
    prompt: str,
    json_response: Optional[bool] = False,
    chat_history: List[Dict[str, str]] | None = None,
) -> Any:
    logging.info(f"Starting ChatGPT_API_with_finish_reason with prompt: {prompt[:200]}...")

    max_retries = 3
    client = LLMClient()

    # build OpenAI-style messages
    messages = (chat_history or []).copy()
    messages.append({"role": "user", "content": prompt})
    for i in range(max_retries):
        try:
            # Optional: token counting (depends on your implementation)
            messages_as_strings = "\n".join(f"{msg['role']}: {msg['content']}" for msg in messages if "content" in msg)
            try:
                logging.debug(f"Attempt {i + 1}/{max_retries} - tokens {count_tokens_mistral(messages_as_strings)}")
            except Exception:
                # don't fail if your token counter is provider-specific
                pass
            unified = client.generate(messages=messages, json_response=json_response)

            logging.info(f"Received response with finish_reason: {unified.finish_reason}")

            if unified.finish_reason == "length":
                return unified.content, "max_output_reached"
            else:
                return unified.content, "finished"

        except Exception as e:
            print("************* Retrying *************")
            logging.warning(f"Retrying after error on attempt {i + 1}: {e}")
            if i < max_retries - 1:
                time.sleep(1)
            else:
                logging.error(f"Max retries reached for prompt: {prompt[:200]}... Last error: {e}")
                return "Error"


def ChatGPT_API(
    prompt: str,
    json_response: Optional[bool] = False,
    chat_history: List[Dict[str, str]] | None = None,
) -> Any:
    """
    Calls the unified LLMClient and returns the assistant's content.
    Preserves retries and the original return contract (str or "Error").
    """
    max_retries = 3
    logging.info(f"Starting ChatGPT_API with prompt: {prompt[:200]}...")
    llm = LLMClient()  # provider is selected via env: LLM_PROVIDER

    # Build OpenAI-style messages
    messages = (chat_history or []).copy()
    messages.append({"role": "user", "content": prompt})

    for i in range(max_retries):
        try:
            unified = llm.generate(messages=messages, json_response=json_response)
            # If needed, you could also inspect: unified.finish_reason / unified.usage / unified.raw_response
            return unified.content

        except Exception as e:
            print("************* Retrying *************")
            logging.error(f"Error on attempt {i + 1}/{max_retries}: {e}")
            if i < max_retries - 1:
                time.sleep(1)
            else:
                logging.error("Max retries reached for prompt: " + prompt)
                return "Error"


async def ChatGPT_API_async(model, prompt, api_key=MISTRAL_API_KEY, endpoint=MISTRAL_ENDPOINT):
    max_retries = 3
    logging.info(f"Starting ChatGPT_API_async with prompt: {prompt[:200]}...")
    messages = [{"role": "user", "content": prompt}]
    for i in range(max_retries):
        try:
            async with openai.AsyncOpenAI(api_key=api_key, base_url=endpoint) as client:
                response = await client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=0,
                )
                return response.choices[0].message.content
        except Exception as e:
            print("************* Retrying *************")
            logging.error(f"Error: {e}")
            if i < max_retries - 1:
                await asyncio.sleep(1)  # Wait for 1s before retrying
            else:
                logging.error("Max retries reached for prompt: " + prompt)
                return "Error"


def get_json_content(response):
    start_idx = response.find("```json")
    if start_idx != -1:
        start_idx += 7
        response = response[start_idx:]

    end_idx = response.rfind("```")
    if end_idx != -1:
        response = response[:end_idx]

    json_content = response.strip()
    return json_content


def extract_json(content: str):
    try:
        logger.info("Start extract_json function with %s", content)
        # First, try to extract JSON enclosed within ```json and ```
        start_idx = content.find("```json")
        if start_idx != -1:
            start_idx += 7  # Adjust index to start after the delimiter
            end_idx = content.rfind("```")
            json_content = content[start_idx:end_idx].strip()
        else:
            # If no delimiters, assume entire content could be JSON
            json_content = content.strip()

        # Clean up common issues that might cause parsing errors
        json_content = json_content.replace("None", "null")  # Replace Python None with JSON null
        json_content = json_content.replace("\n", " ").replace("\r", " ")  # Remove newlines
        json_content = " ".join(json_content.split())  # Normalize whitespace

        logger.info("Cleaned content is %s", json_content)
        # Attempt to parse and return the JSON object
        return json.loads(json_content)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to extract JSON: {e}")
        # Try to clean up the content further if initial parsing fails
        try:
            # Remove any trailing commas before closing brackets/braces
            json_content = json_content.replace(",]", "]").replace(",}", "}")
            return json.loads(json_content)
        except:
            logging.error("Failed to parse JSON even after cleanup")
            return {}
    except Exception as e:
        logging.error(f"Unexpected error while extracting JSON: {e}")
        return {}


def write_node_id(data, node_id=0):
    if isinstance(data, dict):
        data["node_id"] = str(node_id).zfill(4)
        node_id += 1
        for key in list(data.keys()):
            if "nodes" in key:
                node_id = write_node_id(data[key], node_id)
    elif isinstance(data, list):
        for index in range(len(data)):
            node_id = write_node_id(data[index], node_id)
    return node_id


def get_nodes(structure: List[Dict[str, Any]]) -> List[Dict]:
    if isinstance(structure, dict):
        structure_node = copy.deepcopy(structure)
        structure_node.pop("nodes", None)  # Remove children from deepcopy of Tree
        nodes = [structure_node]  # Set nodes as List of Parent Nodes
        for key in list(structure.keys()):
            if "nodes" in key:
                nodes.extend(get_nodes(structure[key]))
        return nodes
    elif isinstance(structure, list):
        nodes = []
        for item in structure:
            nodes.extend(get_nodes(item))
        return nodes


def structure_to_list(structure):
    if isinstance(structure, dict):
        nodes = []
        nodes.append(structure)
        if "nodes" in structure:
            nodes.extend(structure_to_list(structure["nodes"]))
        return nodes
    elif isinstance(structure, list):
        nodes = []
        for item in structure:
            nodes.extend(structure_to_list(item))
        return nodes


def get_first_start_page_from_text(text):
    start_page = -1
    start_page_match = re.search(r"<start_index_(\d+)>", text)
    if start_page_match:
        start_page = int(start_page_match.group(1))
    return start_page


def get_last_start_page_from_text(text):
    start_page = -1
    # Find all matches of start_index tags
    start_page_matches = re.finditer(r"<start_index_(\d+)>", text)
    # Convert iterator to list and get the last match if any exist
    matches_list = list(start_page_matches)
    if matches_list:
        start_page = int(matches_list[-1].group(1))
    return start_page


def sanitize_filename(filename, replacement="-"):
    # In Linux, only '/' and '\0' (null) are invalid in filenames.
    # Null can't be represented in strings, so we only handle '/'.
    return filename.replace("/", replacement)


def get_pdf_name(pdf_path):
    # Extract PDF name
    if isinstance(pdf_path, str):
        pdf_name = os.path.basename(pdf_path)
    elif isinstance(pdf_path, BytesIO):
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        meta = pdf_reader.metadata
        pdf_name = meta.title if meta and meta.title else "Untitled"
        pdf_name = sanitize_filename(pdf_name)
    return pdf_name


class JsonLogger:
    def __init__(self, file_path):
        # Extract PDF name for logger name
        pdf_name = get_pdf_name(file_path)

        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filename = f"{pdf_name}_{current_time}.json"
        os.makedirs("./logs", exist_ok=True)
        # Initialize empty list to store all messages
        self.log_data = []

    def log(self, level, message, **kwargs):
        if isinstance(message, dict):
            self.log_data.append(message)
        else:
            self.log_data.append({"message": message})
        # Add new message to the log data

        # Write entire log data to file
        with open(self._filepath(), "w") as f:
            json.dump(self.log_data, f, indent=2)

    def info(self, message, **kwargs):
        self.log("INFO", message, **kwargs)

    def error(self, message, **kwargs):
        self.log("ERROR", message, **kwargs)

    def debug(self, message, **kwargs):
        self.log("DEBUG", message, **kwargs)

    def exception(self, message, **kwargs):
        kwargs["exception"] = True
        self.log("ERROR", message, **kwargs)

    def _filepath(self):
        return os.path.join("logs", self.filename)


def list_to_tree(data):
    def get_parent_structure(structure):
        """Helper function to get the parent structure code"""
        if not structure:
            return None
        parts = str(structure).split(".")
        return ".".join(parts[:-1]) if len(parts) > 1 else None

    # First pass: Create nodes and track parent-child relationships
    nodes = {}
    root_nodes = []

    for item in data:
        structure = item.get("structure")
        node = {
            "title": item.get("title"),
            "section_number": item.get("structure"),
            "start_index": item.get("start_index"),
            "end_index": item.get("end_index"),
            "nodes": [],
        }

        nodes[structure] = node

        # Find parent
        parent_structure = get_parent_structure(structure)

        if parent_structure:
            # Add as child to parent if parent exists
            if parent_structure in nodes:
                nodes[parent_structure]["nodes"].append(node)
            else:
                root_nodes.append(node)
        else:
            # No parent, this is a root node
            root_nodes.append(node)

    # Helper function to clean empty children arrays
    def clean_node(node):
        if not node["nodes"]:
            del node["nodes"]
        else:
            for child in node["nodes"]:
                clean_node(child)
        return node

    # Clean and return the tree
    return [clean_node(node) for node in root_nodes]


def add_preface_if_needed(data):
    if not isinstance(data, list) or not data:
        return data

    if data[0]["physical_index"] is not None and data[0]["physical_index"] > 1:
        preface_node = {
            "structure": "0",
            "title": "Preface",
            "physical_index": 1,
        }
        data.insert(0, preface_node)
    return data


def get_page_tokens(pdf_path, model="cl100k_base", pdf_parser="PyPDF2"):
    enc = tiktoken.get_encoding(model)
    if pdf_parser == "PyPDF2":
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        page_list = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            token_length = len(enc.encode(page_text))
            page_list.append((page_text, token_length))
        return page_list
    elif pdf_parser == "PyMuPDF":
        if isinstance(pdf_path, BytesIO):
            pdf_stream = pdf_path
            doc = pymupdf.open(stream=pdf_stream, filetype="pdf")
        elif isinstance(pdf_path, str) and os.path.isfile(pdf_path) and pdf_path.lower().endswith(".pdf"):
            doc = pymupdf.open(pdf_path)
        page_list = []
        for page in doc:
            page_text = page.get_text()
            token_length = len(enc.encode(page_text))
            page_list.append((page_text, token_length))
        return page_list
    else:
        raise ValueError(f"Unsupported PDF parser: {pdf_parser}")


def get_text_of_node(pdf_pages, start_page: int, end_page: int, current_node: Optional[str] = None) -> str:
    """
    Extract the text from a contiguous range of PDF pages and, optionally, trim it to the
    content of a specific section (node).

    The Section heading of the node is recognized by an exact match with current_node.
    The heading of the following Section is recognized by the regex:
        `(?m)^\\s*\\d+(?:\\.\\d+)*\\b\\s+[A-Za-z]`
    which matches lines starting with a section number (e.g., `1`, `1.2`, `1.2.3`) followed
    by at least one space and a letter (start of the title). This helps avoid treating a
    bare page number like `2` on its own line as a heading.

    Args:
        pdf_pages: A sequence of page contents.
        start_page (int): 1-based index of the first page to include (inclusive).
        end_page (int): 1-based index of the last page to include (inclusive).
        current_node (Optional[str]): Section number to anchor on (e.g., "1.2", "2", "3.4.5").
                                      If omitted or not found in the text, the concatenated
                                      text of the page range is returned unchanged.

    Returns:
        str: The concatenated page text, optionally trimmed to the current node’s content.

    Edge Cases:
        - If `current_node` is not found, the full concatenated text is returned.
        - Lines that are only digits (e.g., a page number "2") are **not** considered
          headings by the default next-section pattern, helping avoid accidental cuts.
    """
    text = ""
    # First, extract text of all corresponding pages
    for page_num in range(start_page - 1, end_page):
        text += pdf_pages[page_num][0]

    # Second, remove text which comes before the current section number
    if current_node:
        # Build a regex that finds the exact section number at a word boundary
        current_pattern = rf"\b{re.escape(current_node)}\b"

        current_node_match = re.search(current_pattern, text)
        if current_node_match:
            text = text[current_node_match.start() :]  # keep from the section number onwards

            # Third, remove text which is part of the following node
            any_section_pattern = r"(?m)^\s*\d+(?:\.\d+)*\b\s+[A-Za-z]"  # Matches a section heading: start of line, optional spaces, section number (e.g., 1.2.3), then space and a letter

            for i, following_node_match in enumerate(re.finditer(any_section_pattern, text), start=1):
                if i == 2:
                    text = text[: following_node_match.start()]

    return text


def post_processing(structure, end_physical_index):
    # First convert page_number to start_index in flat list
    for i, item in enumerate(structure):
        item["start_index"] = item.get("physical_index")
        if i < len(structure) - 1:
            if structure[i + 1].get("appear_start") == "yes":
                item["end_index"] = structure[i + 1]["physical_index"] - 1
            else:
                item["end_index"] = structure[i + 1]["physical_index"]
        else:
            item["end_index"] = end_physical_index
    tree = list_to_tree(structure)
    if len(tree) != 0:
        return tree
    else:
        ### remove appear_start
        for node in structure:
            node.pop("appear_start", None)
            node.pop("physical_index", None)
        return structure


def clean_structure_post(data):
    if isinstance(data, dict):
        data.pop("page_number", None)
        data.pop("start_index", None)
        data.pop("end_index", None)
        if "nodes" in data:
            clean_structure_post(data["nodes"])
    elif isinstance(data, list):
        for section in data:
            clean_structure_post(section)
    return data


def remove_fields(data, fields=["text"]):
    if isinstance(data, dict):
        return {k: remove_fields(v, fields) for k, v in data.items() if k not in fields}
    elif isinstance(data, list):
        return [remove_fields(item, fields) for item in data]
    return data


def print_toc(tree, indent=0):
    for node in tree:
        print("  " * indent + node["title"])
        if node.get("nodes"):
            print_toc(node["nodes"], indent + 1)


def print_json(data, max_len=40, indent=2):
    def simplify_data(obj):
        if isinstance(obj, dict):
            return {k: simplify_data(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [simplify_data(item) for item in obj]
        elif isinstance(obj, str) and len(obj) > max_len:
            return obj[:max_len] + "..."
        else:
            return obj

    simplified = simplify_data(data)
    print(json.dumps(simplified, indent=indent, ensure_ascii=False))


def remove_structure_text(data):
    if isinstance(data, dict):
        data.pop("text", None)
        if "nodes" in data:
            remove_structure_text(data["nodes"])
    elif isinstance(data, list):
        for item in data:
            remove_structure_text(item)
    return data


def check_token_limit(structure, limit=110000):  # TODO define limit in config
    list = structure_to_list(structure)
    for node in list:
        num_tokens = count_tokens_mistral(node["text"])
        if num_tokens > limit:
            print(f"Node ID: {node['node_id']} has {num_tokens} tokens")
            print("Start Index:", node["start_index"])
            print("End Index:", node["end_index"])
            print("Title:", node["title"])
            print("\n")


def convert_physical_index_to_int(data):
    if isinstance(data, list):
        for i in range(len(data)):
            # Check if item is a dictionary and has 'physical_index' key
            if isinstance(data[i], dict) and "physical_index" in data[i]:
                if isinstance(data[i]["physical_index"], str):
                    if data[i]["physical_index"].startswith("<physical_index_"):
                        data[i]["physical_index"] = int(data[i]["physical_index"].split("_")[-1].rstrip(">").strip())
                    elif data[i]["physical_index"].startswith("physical_index_"):
                        data[i]["physical_index"] = int(data[i]["physical_index"].split("_")[-1].strip())
    elif isinstance(data, str):
        if data.startswith("<physical_index_"):
            data = int(data.split("_")[-1].rstrip(">").strip())
        elif data.startswith("physical_index_"):
            data = int(data.split("_")[-1].strip())
        # Check data is int
        if isinstance(data, int):
            return data
        else:
            return None
    return data


def convert_page_to_int(data):
    for item in data:
        if "page" in item and isinstance(item["page"], str):
            try:
                item["page"] = int(item["page"])
            except ValueError:
                # Keep original value if conversion fails
                pass
    return data


def add_node_text(node, pdf_pages):
    if isinstance(node, dict):
        start_page = node.get("start_index")
        end_page = node.get("end_index")
        node["text"] = get_text_of_node(pdf_pages, start_page, end_page, node["section_number"])
        if "nodes" in node:
            add_node_text(node["nodes"], pdf_pages)
    elif isinstance(node, list):
        for index in range(len(node)):
            add_node_text(node[index], pdf_pages)
    return


def add_node_text_with_labels(node, pdf_pages):  # seems like dead code!
    if isinstance(node, dict):
        start_page = node.get("start_index")
        end_page = node.get("end_index")
        node["text"] = get_text_of_pdf_pages_with_labels(pdf_pages, start_page, end_page)
        if "nodes" in node:
            add_node_text_with_labels(node["nodes"], pdf_pages)
    elif isinstance(node, list):
        for index in range(len(node)):
            add_node_text_with_labels(node[index], pdf_pages)
    return


async def generate_node_summary(node, model=None):
    prompt = f"""You are given a part of a document, your task is to generate a description of the partial document about what are main points covered in the partial document.

    Partial Document Text: {node["text"]}
    
    Directly return the description, do not include any other text.
    """
    response = await ChatGPT_API_async(model, prompt)
    return response


async def generate_summaries_for_structure(structure, model=None):
    nodes = structure_to_list(structure)
    tasks = [generate_node_summary(node, model=model) for node in nodes]
    summaries = await asyncio.gather(*tasks)

    for node, summary in zip(nodes, summaries):
        node["summary"] = summary
    return structure


def create_clean_structure_for_description(structure):
    """
    Create a clean structure for document description generation,
    excluding unnecessary fields like 'text'.
    """
    if isinstance(structure, dict):
        clean_node = {}
        # Only include essential fields for description
        for key in ["title", "node_id", "summary", "prefix_summary"]:
            if key in structure:
                clean_node[key] = structure[key]

        # Recursively process child nodes
        if "nodes" in structure and structure["nodes"]:
            clean_node["nodes"] = create_clean_structure_for_description(structure["nodes"])

        return clean_node
    elif isinstance(structure, list):
        return [create_clean_structure_for_description(item) for item in structure]
    else:
        return structure


def generate_doc_description(structure, model=None):
    prompt = f"""Your are an expert in generating descriptions for a document.
    You are given a structure of a document. Your task is to generate a one-sentence description for the document, which makes it easy to distinguish the document from other documents.
        
    Document Structure: {structure}
    
    Directly return the description, do not include any other text.
    """
    response = ChatGPT_API(model, prompt)
    return response


def reorder_dict(data, key_order):
    if not key_order:
        return data
    return {key: data[key] for key in key_order if key in data}


def format_structure(structure, order=None):
    if not order:
        return structure
    if isinstance(structure, dict):
        if "nodes" in structure:
            structure["nodes"] = format_structure(structure["nodes"], order)
        if not structure.get("nodes"):
            structure.pop("nodes", None)
        structure = reorder_dict(structure, order)
    elif isinstance(structure, list):
        structure = [format_structure(item, order) for item in structure]
    return structure


class ConfigLoader:
    def __init__(self, default_path: str = None):
        if default_path is None:
            default_path = Path(__file__).parent / "config.yaml"
        self._default_dict = self._load_yaml(default_path)

    @staticmethod
    def _load_yaml(path):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def _validate_keys(self, user_dict):
        unknown_keys = set(user_dict) - set(self._default_dict)
        if unknown_keys:
            raise ValueError(f"Unknown config keys: {unknown_keys}")

    def load(self, user_opt=None) -> config:
        """
        Load the configuration, merging user options with default values.
        """
        if user_opt is None:
            user_dict = {}
        elif isinstance(user_opt, config):
            user_dict = vars(user_opt)
        elif isinstance(user_opt, dict):
            user_dict = user_opt
        else:
            raise TypeError("user_opt must be dict, config(SimpleNamespace) or None")

        self._validate_keys(user_dict)
        merged = {**self._default_dict, **user_dict}
        return config(**merged)
