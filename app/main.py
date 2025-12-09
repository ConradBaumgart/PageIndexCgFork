import os
from contextlib import asynccontextmanager
from typing import Dict, List

from fastapi import FastAPI, File, UploadFile

from app.logging_config import get_logger
from app.services.list_documents import list_documents
from app.services.upload_document import handle_upload_document

logger = get_logger(__name__)

GENERATED_TREES_FOLDER = "app/data/generated_trees"
ORIGINAL_DOCUMENTS_FOLDER = "app/data/original_documents"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    os.makedirs(GENERATED_TREES_FOLDER, exist_ok=True)
    os.makedirs(GENERATED_TREES_FOLDER, exist_ok=True)
    logger.info("Application starting up...")
    yield
    # Shutdown
    logger.info("Application shutting down...")


app = FastAPI(lifespan=lifespan, title="Information Retrieval Service")


@app.get("/health_check")
def health_check() -> Dict[str, str]:
    return {"status": "ok"}


@app.get("/list_available_documents")
async def list_available_documents() -> List[Dict[str, str]]:
    """
    List all documents which are available for information retrieval.
    """
    return list_documents()


@app.get("/query_documents")
async def query_documents(query: str, documents: list[str]) -> List[Dict[str, str]]:
    """
    (Mock) Return content from documents relevant to the query.
    """
    result = []
    return {"uploaded": result}


@app.post("/upload_document")
async def upload_document(file: UploadFile = File(...)) -> Dict[str, str]:
    """
    Upload a single PDF document to process it and make it available for information retrieval.
    """
    result = await handle_upload_document(file)
    return result
