from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.logging_config import get_logger
from app.api import get_nodes, health, list_trees, upload_document

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Application starting up...")
    yield
    # Shutdown
    logger.info("Application shutting down...")

app = FastAPI(lifespan=lifespan, title="Information Retrieval Service")

# Include routers
app.include_router(health.router)
app.include_router(upload_document.router)
app.include_router(list_trees.router)
app.include_router(get_nodes.router)
