import os
import requests

#BASE_URL = os.getenv("IRS_BASE_URL", "http://localhost:8000")
BASE_URL = "http://localhost:8000/"

session = requests.Session()
session.headers.update({"Accept": "application/json"})

timeout = (5, 240)  # (connect, read) Sekunden


### GET list_available_documents

r = session.get(f"{BASE_URL}/list_available_documents", timeout=timeout)
r.raise_for_status()
docs = r.json()  # list[dict[str,str]]
print("################## list available documents ########################")
print(docs)


### GET list_available_documents

query = "Worum geht es im Dokument?"
documents = ["MIL-STD-1316F.pdf"]  # mind. 1 Name; wiederholter Query-Param

params = {"query": query, "documents": documents}
r = session.get(f"{BASE_URL}/query_documents", params=params, timeout=timeout)

# 422 sauber behandeln:
if r.status_code == 422:
    print("Validation Error:", r.json())
    r.raise_for_status()

r.raise_for_status()
print("################## query documents ########################")
print(r.json())  # list[dict[Any,Any]]

### POST upload_document

from pathlib import Path

pdf_path = "app/data/original_documents/paper_llm_neutrality.pdf"

files = {"file": (Path(pdf_path).name, open(pdf_path, "rb"), "application/pdf")}

r = session.post(f"{BASE_URL}/upload_document", files=files, timeout=timeout)

# 422 sauber behandeln:
if r.status_code == 422:
    print("Validation Error:", r.json())
    r.raise_for_status()

r.raise_for_status()
print("################## query documents ########################")
print(r.json())  # dict[str,str]
