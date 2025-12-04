
from pathlib import Path
import json
from typing import List, Dict, Any
from fastapi import APIRouter

RESULTS_DIR = Path("results")


def list_result_jsons() -> List[str]:
    """
    Scan the fixed `results/` directory recursively for `.json` files and return a list
    of `doc_name` strings.
    """
    if not RESULTS_DIR.exists() or not RESULTS_DIR.is_dir():
        return []

    doc_names: List[str] = []

    for json_path in RESULTS_DIR.rglob("*.json"):
        try:
            with json_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            doc_name = data.get("doc_name")
            if isinstance(doc_name, str) and doc_name.strip():
                doc_names.append(doc_name.strip())
        except (json.JSONDecodeError, OSError):
            continue

    doc_names.sort(key=lambda x: x.lower())
    return doc_names


router = APIRouter(prefix="", tags=["list-trees"])


