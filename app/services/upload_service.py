
from fastapi import UploadFile, HTTPException
from typing import Dict
import os
import json
from pageindex.page_index import page_index_main

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data")

async def handle_document_upload(file: UploadFile) -> Dict[str, int]:
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

    opt = {
        "model": 'gpt-4o-2024-11-20',
        "toc_check_page_num": 20,
        "max_page_num_each_node": 10,
        "max_token_num_each_node": 20000,
        "if_add_node_id": "yes",
        "if_add_node_summary": "yes",
        "if_add_doc_description":"yes",
        "if_add_node_text": "yes"
    }

    # Process the PDF
    toc_with_page_number = page_index_main(file_path, opt)
    print('Parsing done, saving to file...')
    
    # Save results
    pdf_name = os.path.splitext(os.path.basename(file_path))[0]    
    output_dir = './results'
    output_file = f'{output_dir}/{pdf_name}_structure.json'
    os.makedirs(output_dir, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(toc_with_page_number, f, indent=2)
    
    print(f'Tree structure saved to: {output_file}')
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}
