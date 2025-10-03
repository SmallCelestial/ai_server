import os
from functools import lru_cache
from dataclasses import dataclass


def _to_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y", "on"}


def _to_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


@dataclass(frozen=True)
class Settings:
    app_name: str = "AI Server"
    version: str = "0.2.0"
    environment: str = "local"
    debug: bool = False
    api_prefix: str = ""
    cors_origins: tuple[str, ...] = ()


@lru_cache
def get_settings() -> "Settings":
    return Settings(
        app_name=os.getenv("APP_NAME", "AI Server"),
        version=os.getenv("APP_VERSION", "0.2.0"),
        environment=os.getenv("ENVIRONMENT", "local"),
        debug=_to_bool(os.getenv("DEBUG"), False),
        api_prefix=os.getenv("API_PREFIX", ""),
        cors_origins=tuple(_to_list(os.getenv("CORS_ORIGINS"))),
    )
