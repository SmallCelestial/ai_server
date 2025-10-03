from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Optional

router = APIRouter()


class GreetRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    language: Optional[str] = Field(default="en", description="ISO language code like en, es, fr")


class GreetResponse(BaseModel):
    message: str
    language: str


@router.post("/greet", response_model=GreetResponse, tags=["greet"]) 
async def greet(req: GreetRequest):
    name = req.name.strip()
    lang = (req.language or "en").lower()
    greetings = {
        "en": "Hello",
        "es": "Hola",
        "fr": "Bonjour",
        "de": "Hallo",
        "pl": "Cześć",
    }
    salutation = greetings.get(lang, greetings["en"])
    return GreetResponse(message=f"{salutation} {name}", language=lang)


class NotifyRequest(BaseModel):
    recipient: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)


class NotifyResponse(BaseModel):
    status: str


def _send_notification(recipient: str, message: str) -> None:
    # Placeholder: emulate sending a notification by printing/logging.
    print(f"[notify] to={recipient} msg={message}")


@router.post("/notify", response_model=NotifyResponse, tags=["greet"]) 
async def notify(req: NotifyRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(_send_notification, req.recipient, req.message)
    return NotifyResponse(status="scheduled")
