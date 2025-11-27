
from fastapi import FastAPI
from app.api import health, upload_document  # Import both routers

app = FastAPI(title="My FastAPI Service")

# Include routers
app.include_router(health.router)
app.include_router(upload_document.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI backend!"}
