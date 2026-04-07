from fastapi import APIRouter, HTTPException
from apps.schemas import TTSRequest
from apps.services.tts_service import synthesize_speech

router = APIRouter(prefix="/text-to-speech", tags=["tts"])


@router.post("")
async def text_to_speech(request: TTSRequest):
    try:
        filename = synthesize_speech(request.text)
        return {"audio_url": f"/generated-audio/{filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
