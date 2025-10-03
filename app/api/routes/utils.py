from datetime import datetime, timezone
from typing import Any, Dict, Optional

from fastapi import APIRouter, Body, Query, Request
from pydantic import BaseModel

router = APIRouter()


class TimeResponse(BaseModel):
    iso: str
    epoch_ms: int
    timezone: str


@router.get("/time", response_model=TimeResponse, tags=["utils"]) 
async def get_time():
    now = datetime.now(timezone.utc)
    return TimeResponse(iso=now.isoformat(), epoch_ms=int(now.timestamp() * 1000), timezone="UTC")


class EchoResponse(BaseModel):
    query: Dict[str, Any]
    body: Optional[Dict[str, Any]]


@router.get("/echo", response_model=EchoResponse, tags=["utils"]) 
async def echo_get(request: Request, q: Optional[str] = Query(default=None, description="Optional query")):
    # Return all query params; q is just a documented example
    qp = dict(request.query_params)
    return EchoResponse(query=qp, body=None)


@router.post("/echo", response_model=EchoResponse, tags=["utils"]) 
async def echo_post(payload: Dict[str, Any] = Body(default=None)):
    return EchoResponse(query={}, body=payload)
