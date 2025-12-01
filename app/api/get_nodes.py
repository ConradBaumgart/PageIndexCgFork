from fastapi import APIRouter, Query
from typing import List

router = APIRouter(prefix="/get_nodes")

@router.get("/")
async def get_nodes(question: str = Query(..., description="User question")) -> List[str]:
    """
    (Draft! Mock) Return a list of nodes based on the input question.
    Currently returns an empty list as a placeholder.
    """
    # In a real implementation, you'd process the question and fetch related nodes.
    return []
