from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)
register_exception_handlers(app)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to ReqForge AI"
    }