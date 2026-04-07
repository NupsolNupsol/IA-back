import re


def clean_text_for_tts(text: str) -> str:
    if not text:
        return ""

    cleaned = text

    # Remove fenced code blocks
    cleaned = re.sub(r"```.*?```", " ", cleaned, flags=re.DOTALL)

    # Remove inline code
    cleaned = re.sub(r"`([^`]*)`", r"\1", cleaned)

    # Convert markdown links [text](url) -> text
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)

    # Remove bold/italic markers
    cleaned = re.sub(r"\*\*([^*]+)\*\*", r"\1", cleaned)
    cleaned = re.sub(r"\*([^*]+)\*", r"\1", cleaned)
    cleaned = re.sub(r"__([^_]+)__", r"\1", cleaned)
    cleaned = re.sub(r"_([^_]+)_", r"\1", cleaned)

    # Remove markdown headings
    cleaned = re.sub(r"^\s*#{1,6}\s*", "", cleaned, flags=re.MULTILINE)

    # Remove blockquote markers
    cleaned = re.sub(r"^\s*>\s?", "", cleaned, flags=re.MULTILINE)

    # Remove list bullets
    cleaned = re.sub(r"^\s*[-*+]\s+", "", cleaned, flags=re.MULTILINE)

    # Remove numbered list markers like "1. "
    cleaned = re.sub(r"^\s*\d+\.\s+", "", cleaned, flags=re.MULTILINE)

    # Collapse extra whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    return cleaned
