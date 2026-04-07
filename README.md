Nupsol AI Assistant Backend

FastAPI backend for the Nupsol AI Assistant.

This backend provides:

- Text chat with a local AI model through Ollama
- Speech-to-text using Faster Whisper
- Text-to-speech using Piper
- Audio responses
- Realtime push-to-talk voice interaction through WebSocket

---

## Requirements

Before running the backend, make sure the machine has:

- Python 3.11+ installed
- Ollama installed and running
- A pulled Ollama model
- Piper voice model downloaded locally

---

## Project Structure

```text
backend/
├── apps/
│   ├── config.py
│   ├── main.py
│   ├── schemas.py
│   ├── routers/
│   │   ├── chat.py
│   │   ├── realtime.py
│   │   ├── speech.py
│   │   └── tts.py
│   ├── services/
│   │   ├── ollama_service.py
│   │   ├── realtime_session.py
│   │   ├── stt_service.py
│   │   └── tts_service.py
│   └── utils/
├── generated_audio/
├── tmp_audio/
├── requirements.txt
├── .env
└── README.md
Setup Instructions
1. Install Ollama
Install Ollama on the machine, then pull the model used by the project:

Bash
ollama pull qwen2.5:7b
Make sure Ollama is running locally. You can test it with:

Bash
ollama run qwen2.5:7b
2. Install Piper Voice Model
This project expects the Piper voice model to exist at:
C:\piper\voices\en_US-lessac-medium.onnx

and its config file at:
C:\piper\voices\en_US-lessac-medium.onnx.json

If a different Piper model path is used, update the .env file accordingly.

3. Create .env
Create a file named .env inside the backend/ folder with this content:

Extrait de code
OLLAMA_URL=http://localhost:11434/api/chat
MODEL_NAME=qwen2.5:7b
REQUEST_TIMEOUT=180
DEFAULT_SYSTEM_PROMPT=You are a helpful AI assistant. Respond in the same language as the user unless explicitly asked otherwise.
WHISPER_MODEL=small
PIPER_MODEL=C:/piper/voices/en_US-lessac-medium.onnx
GENERATED_AUDIO_DIR=generated_audio
4. Create Virtual Environment
From inside the backend/ folder:

Windows

DOS
python -m venv venv
venv\Scripts\activate.bat
macOS / Linux

Bash
python3 -m venv venv
source venv/bin/activate
5. Install Python Dependencies
With the virtual environment activated:

DOS
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install piper-tts
python -m pip install "uvicorn[standard]" websockets wsproto
6. Run the Backend
From inside backend/:

Windows

DOS
venv\Scripts\activate.bat
python -m uvicorn apps.main:app --reload
macOS / Linux

Bash
source venv/bin/activate
python -m uvicorn apps.main:app --reload
The backend will run at: http://127.0.0.1:8000

Swagger docs: http://127.0.0.1:8000/docs

Available Endpoints
Health check: GET /health

Text chat: POST /chat

Voice upload chat: POST /chat/audio

Speech to text: POST /speech-to-text

Text to speech: POST /text-to-speech
```
