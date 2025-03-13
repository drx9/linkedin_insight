from fastapi import FastAPI
from app.api.endpoints import router as api_router

# Create the FastAPI app instance
app = FastAPI()

# Include the API router
app.include_router(api_router, prefix="/api")