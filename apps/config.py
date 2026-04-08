import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5:7b")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "180"))

# This default is overridden by the frontend which sends the full medical system prompt.
# It acts as a safety fallback only.
DEFAULT_SYSTEM_PROMPT = os.getenv(
    "DEFAULT_SYSTEM_PROMPT",
    "You are MedAssist AI, an exclusive clinical AI assistant for healthcare professionals. "
    "You only respond to medical and clinical questions. "
    "For any non-medical question, respond: "
    "'I am exclusively specialized in medical assistance. I can help with clinical questions, "
    "medication guidance, prescription drafting, or other healthcare topics.' "
    "Be professional, empathetic, and precise.",
)

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")
PIPER_MODEL = os.getenv("PIPER_MODEL", "")
GENERATED_AUDIO_DIR = os.getenv("GENERATED_AUDIO_DIR", "generated_audio")

os.makedirs(GENERATED_AUDIO_DIR, exist_ok=True)
