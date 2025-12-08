from fastapi import UploadFile, HTTPException
from typing import Dict
import os
import json
from pageindex.page_index import page_index_main
from app.models.page_index_options import PageIndexOptions
from app.logging_config import get_logger

logger = get_logger(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data")


async def handle_document_upload(file: UploadFile) -> Dict[str, str]:
    """
    Validate and process a single uploaded PDF file.
    """

    # Validate PDF content type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail=f"{file.filename} is not a PDF file")

    # Optional: Validate filename extension
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must have .pdf extension")

    # Ensure data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    # Define file path
    file_path = os.path.join(DATA_DIR, file.filename)

    # Save file to disk
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    opt = PageIndexOptions()

    # Process the PDF
    toc_with_page_number = await page_index_main(file_path, opt)
    logger.info(f"Parsing done, saving file {file_path}")

    # Save results
    pdf_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = "./results"
    output_file = f"{output_dir}/{pdf_name}_structure.json"
    os.makedirs(output_dir, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(toc_with_page_number, f, indent=2)

    logger.info(f"Tree structure saved to: {output_file}")

    return {"filename": file.filename}
