import os
import subprocess
import sys
import uuid
from apps.config import PIPER_MODEL, GENERATED_AUDIO_DIR
from apps.utils.text_for_tts import clean_text_for_tts


def synthesize_speech(text: str) -> str:
    if not PIPER_MODEL:
        raise RuntimeError("PIPER_MODEL is not configured.")

    if not os.path.isfile(PIPER_MODEL):
        raise RuntimeError(f"Piper model not found: {PIPER_MODEL}")

    os.makedirs(GENERATED_AUDIO_DIR, exist_ok=True)

    speech_text = clean_text_for_tts(text)

    if not speech_text:
        raise RuntimeError("No valid text to synthesize after cleaning.")

    output_filename = f"{uuid.uuid4()}.wav"
    output_path = os.path.join(GENERATED_AUDIO_DIR, output_filename)

    cmd = [
        sys.executable,
        "-m",
        "piper",
        "--model",
        PIPER_MODEL,
        "--output_file",
        output_path,
    ]

    process = subprocess.run(cmd, input=speech_text, text=True, capture_output=True)

    if process.returncode != 0:
        raise RuntimeError(process.stderr or "Piper TTS failed.")

    if not os.path.isfile(output_path):
        raise RuntimeError("Piper finished but no audio file was generated.")

    return output_filename
