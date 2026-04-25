import re
import json


def clean_text(text: str) -> str:
    if not text:
        return ""

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_text(text: str) -> str:
    return clean_text(text).lower()


def load_json(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
