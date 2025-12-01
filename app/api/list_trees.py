from fastapi import APIRouter
from typing import List

router = APIRouter(prefix="/list_trees")

@router.get("/")
async def list_trees() -> List[str]:
    """
    (Draft! Mock) Return a list of tree titles.
    Currently returns an empty list as a placeholder.
    """
    return []
