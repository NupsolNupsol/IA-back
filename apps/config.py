import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5:7b")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "180"))

DEFAULT_SYSTEM_PROMPT = os.getenv(
    "DEFAULT_SYSTEM_PROMPT",
    "You are a helpful AI assistant. Respond in the same language as the user unless explicitly asked otherwise.",
)

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")
PIPER_MODEL = os.getenv("PIPER_MODEL", "")
GENERATED_AUDIO_DIR = os.getenv("GENERATED_AUDIO_DIR", "generated_audio")

os.makedirs(GENERATED_AUDIO_DIR, exist_ok=True)
