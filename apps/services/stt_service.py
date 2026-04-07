from faster_whisper import WhisperModel
from apps.config import WHISPER_MODEL

model = WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8")


def transcribe_audio(file_path: str):
    segments, info = model.transcribe(file_path)

    text_parts = []
    for segment in segments:
        if segment.text:
            text_parts.append(segment.text.strip())

    return {
        "text": " ".join(text_parts).strip(),
        "language": getattr(info, "language", None),
    }
