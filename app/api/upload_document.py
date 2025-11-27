
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List

router = APIRouter(prefix="/upload_document", tags=["upload"])

@router.post("/")
async def upload_documents(files: List[UploadFile] = File(...)):
    """
    Upload one or multiple PDF documents.
    """
    uploaded_files = []
    for file in files:
        # Check file type
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail=f"{file.filename} is not a PDF file")

        # Read file content (optional)
        content = await file.read()
        uploaded_files.append({"filename": file.filename, "size": len(content)})

    return {"uploaded": uploaded_files}
