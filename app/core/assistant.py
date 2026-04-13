from app.core.memory import clear_memory
from app.llm.ollama_llm import conversation_history

def run_assistant(listen, think, speak):
    print("Jarvis online. Type 'exit' to quit.")
    print("Type 'clear memory' to reset memory.\n")
    while True:
        user_input = listen()
        if user_input.lower() in {"exit", "quit"}:
            speak("Goodbye.")
            break
        if user_input.lower() == "clear memory":
            clear_memory()
            conversation_history.clear()   # 👈 THIS LINE IS KEY
            speak("Memory cleared.")
            continue
        reply = think(user_input)
        speak(reply)