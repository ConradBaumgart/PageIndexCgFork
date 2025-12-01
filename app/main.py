from fastapi import FastAPI
from app.api import get_nodes, health, list_trees, upload_document

app = FastAPI(title="Information Retrieval Service")

# Include routers
app.include_router(health.router)
app.include_router(upload_document.router)
app.include_router(list_trees.router)
app.include_router(get_nodes.router)
