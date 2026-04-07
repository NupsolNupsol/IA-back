import os
import uuid
from fastapi import UploadFile


async def save_upload_file(upload_file: UploadFile, folder: str = "tmp_audio") -> str:
    os.makedirs(folder, exist_ok=True)

    ext = os.path.splitext(upload_file.filename or "")[1] or ".webm"
    file_path = os.path.join(folder, f"{uuid.uuid4()}{ext}")

    with open(file_path, "wb") as f:
        content = await upload_file.read()
        f.write(content)

    return file_path
