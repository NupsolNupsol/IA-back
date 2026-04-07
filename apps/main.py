from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from apps.config import MODEL_NAME, GENERATED_AUDIO_DIR
from apps.routers.chat import router as chat_router
from apps.routers.speech import router as speech_router
from apps.routers.tts import router as tts_router

app = FastAPI(title="Local AI Assistant Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/generated-audio",
    StaticFiles(directory=GENERATED_AUDIO_DIR),
    name="generated-audio",
)

app.include_router(chat_router)
app.include_router(speech_router)
app.include_router(tts_router)


@app.get("/health")
async def health():
    return {"status": "ok", "model": MODEL_NAME}
