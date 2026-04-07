from pydantic import BaseModel, Field
from typing import List, Optional


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    history: List[Message] = Field(default_factory=list)
    system_prompt: Optional[str] = None
    temperature: float = 0.7
    speak_response: bool = False


class ChatResponse(BaseModel):
    model: str
    user_text: str
    assistant_text: str
    audio_url: Optional[str] = None


class STTResponse(BaseModel):
    text: str
    language: Optional[str] = None


class TTSRequest(BaseModel):
    text: str
