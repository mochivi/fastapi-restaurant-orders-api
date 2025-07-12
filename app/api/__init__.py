from fastapi import APIRouter

from app.api.routes import v1router

api_router = APIRouter(prefix="/api")
api_router.include_router(v1router)