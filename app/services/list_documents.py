import json
from pathlib import Path
from typing import Dict, List

RESULTS_DIR = Path("app/data/generated_trees")


def list_documents() -> List[Dict[str, str]]:
    """
    Scan the fixed `app/data/generated_trees/` directory recursively for `.json` files and return a list
    of `doc_name` strings.
    """
    if not RESULTS_DIR.exists() or not RESULTS_DIR.is_dir():
        return []

    doc_infos: List[Dict[str, str]] = []

    for json_path in RESULTS_DIR.rglob("*.json"):
        try:
            with json_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            doc_name = data.get("doc_name")
            doc_description = data.get("doc_description")
            if isinstance(doc_name, str) and isinstance(doc_description, str):
                doc_infos.append({"doc_name": doc_name, "doc_description": doc_description})
        except (json.JSONDecodeError, OSError):
            continue

    return doc_infos
