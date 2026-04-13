import requests
from app.core.memory import load_memory, save_memory
conversation_history = load_memory()

def ask_llm(prompt: str) -> str:
    global conversation_history
    conversation_history.append(f"User: {prompt}")
    full_prompt = "\n".join(conversation_history) + "\nAssistant:"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": full_prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        reply = response.json()["response"].strip()
        conversation_history.append(f"Assistant: {reply}")
        save_memory(conversation_history)
        return reply
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {e}"