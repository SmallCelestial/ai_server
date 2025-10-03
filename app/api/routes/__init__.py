from fastapi import APIRouter
from .root import router as root_router
from .health import router as health_router
from .utils import router as utils_router
from .greet import router as greet_router
from .meta import router as meta_router

api_router = APIRouter()
api_router.include_router(root_router)
api_router.include_router(health_router)
api_router.include_router(utils_router)
api_router.include_router(greet_router)
api_router.include_router(meta_router)

__all__ = ["api_router"]
