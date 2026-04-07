import os
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from apps.schemas import STTResponse, ChatResponse, Message
from apps.utils.audio import save_upload_file
from apps.services.stt_service import transcribe_audio
from apps.services.ollama_service import chat_with_model
from apps.services.tts_service import synthesize_speech

router = APIRouter(tags=["speech"])


@router.post("/speech-to-text", response_model=STTResponse)
async def speech_to_text(audio: UploadFile = File(...)):
    file_path = None
    try:
        file_path = await save_upload_file(audio)
        result = transcribe_audio(file_path)
        return STTResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)


@router.post("/chat/audio", response_model=ChatResponse)
async def chat_audio(
    audio: UploadFile = File(...),
    system_prompt: str | None = Form(None),
    speak_response: bool = Form(False),
):
    file_path = None
    try:
        file_path = await save_upload_file(audio)

        stt_result = transcribe_audio(file_path)
        user_text = stt_result["text"]

        chat_result = await chat_with_model(
            user_message=user_text, history=[], system_prompt=system_prompt
        )

        audio_url = None
        if speak_response:
            filename = synthesize_speech(chat_result["assistant_text"])
            audio_url = f"/generated-audio/{filename}"

        return ChatResponse(
            model=chat_result["model"],
            user_text=user_text,
            assistant_text=chat_result["assistant_text"],
            audio_url=audio_url,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
