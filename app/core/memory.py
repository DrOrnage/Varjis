import json
import os
from typing import List

MEMORY_FILE = "memory.json"
MAX_MESSAGES = 20

def load_memory() -> List[str]:
    # Load conversation history from memory.json.
    # Returns an empty list if the file does not exist or is invalid.
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list) and all(isinstance(item, str) for item in data):
            return data
        return []
    except (json.JSONDecodeError, OSError):
        return []


def save_memory(history: List[str]) -> None:
    # Save only the most recent MAX_MESSAGES items to memory.json.
    trimmed_history = history[-MAX_MESSAGES:]
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(trimmed_history, file, indent=2, ensure_ascii=False)
    except OSError:
        pass

def clear_memory() -> None:
    # Delete memory.json if it exists.
    if os.path.exists(MEMORY_FILE):
        try:
            os.remove(MEMORY_FILE)
        except OSError:
            pass