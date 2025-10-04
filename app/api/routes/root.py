from fastapi import APIRouter
from pydantic import BaseModel


class Message(BaseModel):
    message: str


router = APIRouter()


@router.get("/", response_model=Message, tags=["root"])
async def root():
    return Message(message="Hello World version 1.0.2")


@router.get("/hello/{name}", response_model=Message, tags=["root"])
async def say_hello(name: str):
    return Message(message=f"Hello {name}")
