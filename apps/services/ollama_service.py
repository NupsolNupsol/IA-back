import httpx
from apps.config import OLLAMA_URL, MODEL_NAME, REQUEST_TIMEOUT, DEFAULT_SYSTEM_PROMPT


async def chat_with_model(
    user_message: str,
    history: list,
    system_prompt: str | None = None,
    temperature: float = 0.7,
):
    messages = []

    final_system_prompt = system_prompt or DEFAULT_SYSTEM_PROMPT
    if final_system_prompt:
        messages.append({"role": "system", "content": final_system_prompt})

    for msg in history:
        messages.append({"role": msg.role, "content": msg.content})

    messages.append({"role": "user", "content": user_message})

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False,
        "options": {"temperature": temperature},
    }

    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
        response = await client.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()

    return {
        "model": data.get("model", MODEL_NAME),
        "assistant_text": data["message"]["content"].strip(),
    }
