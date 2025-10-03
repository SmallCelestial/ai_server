from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import get_settings

router = APIRouter()


class HealthStatus(BaseModel):
    status: str


@router.get("/health/liveness", response_model=HealthStatus, tags=["health"]) 
async def liveness():
    return HealthStatus(status="ok")


@router.get("/health/readiness", response_model=HealthStatus, tags=["health"]) 
async def readiness():
    # In a more advanced app, check DB connections or external services.
    # Here, we just verify settings can be loaded.
    _ = get_settings()
    return HealthStatus(status="ready")
