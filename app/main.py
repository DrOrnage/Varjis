from app.core.assistant import run_assistant

# Choose your modules here
from app.stt.vosk_stt import listen
from app.tts.print_tts import speak

from app.llm.ollama_llm import ask_llm

if __name__ == "__main__":
    run_assistant(listen, ask_llm, speak)