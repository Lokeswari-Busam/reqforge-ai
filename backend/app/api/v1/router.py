from fastapi import APIRouter

from app.api.v1.endpoints import auth
from app.api.v1.endpoints import project
from app.api.v1.endpoints import document

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(project.router)
api_router.include_router(document.router)