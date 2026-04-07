from fastapi import APIRouter, HTTPException
from apps.schemas import ChatRequest, ChatResponse
from apps.services.ollama_service import chat_with_model
from apps.services.tts_service import synthesize_speech

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        result = await chat_with_model(
            user_message=request.message,
            history=request.history,
            system_prompt=request.system_prompt,
            temperature=request.temperature,
        )

        audio_url = None
        if request.speak_response:
            filename = synthesize_speech(result["assistant_text"])
            audio_url = f"/generated-audio/{filename}"

        return ChatResponse(
            model=result["model"],
            user_text=request.message,
            assistant_text=result["assistant_text"],
            audio_url=audio_url,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
