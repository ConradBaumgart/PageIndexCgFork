from fastapi import APIRouter, UploadFile, File
from app.services.list_trees_service import list_result_jsons

router = APIRouter()

@router.get("/list-trees")
async def get_list_trees():
    """
    Docstring for get_list_trees
    """
    return list_result_jsons()