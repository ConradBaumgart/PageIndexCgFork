from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import handle_document_upload

router = APIRouter(prefix="/upload_document")

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a single PDF document and generate a PageIndex tree.
    """
    result = await handle_document_upload(file)
    return {"uploaded": result}
