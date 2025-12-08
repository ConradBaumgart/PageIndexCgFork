from fastapi import FastAPI, File, HTTPException, UploadFile
from contextlib import asynccontextmanager
from typing import Dict, List
from app.logging_config import get_logger
from app.services.list_trees_service import list_result_jsons
from app.services.upload_service import handle_document_upload

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Application starting up...")
    yield
    # Shutdown
    logger.info("Application shutting down...")


app = FastAPI(lifespan=lifespan, title="Information Retrieval Service")


@app.get("/health_check")
def health_check() -> Dict[str, str]:
    return {"status": "ok"}


@app.get("/list_trees")
async def get_list_trees() -> List[Dict[str, str]]:
    """
    List all documents which are available for information retrieval.
    """
    return list_result_jsons()


@app.get("/get_nodes")
async def list_nodes(query: str, documents: list[str]) -> List[Dict[str, str]]:
    """
    (Mock) Return nodes from documents based on the query.
    """
    result = []
    return {"uploaded": result}


@app.post("/upload_documents")
async def upload_document(file: UploadFile = File(...)) -> Dict[str, str]:
    """
    Upload a single PDF document and generate a PageIndex tree for information retrieval.
    """
    result = await handle_document_upload(file)
    return result