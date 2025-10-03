from datetime import datetime, timezone
from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import get_settings

router = APIRouter()


class AppInfo(BaseModel):
    name: str
    version: str
    environment: str
    server_time: str


@router.get("/info", response_model=AppInfo, tags=["meta"]) 
async def info():
    settings = get_settings()
    now = datetime.now(timezone.utc).isoformat()
    return AppInfo(name=settings.app_name, version=settings.version, environment=settings.environment, server_time=now)
