# Varjis (Budget Jarvis)

A local voice assistant inspired by Jarvis from Iron Man.

This project uses:
- Local LLM (Ollama)
- Persistent memory
- Modular design (STT → LLM → TTS)

## Features

- Chat with a local AI (no API cost)
- Remembers previous conversations
- Modular architecture (easy to swap components)
- Speech input support (WIP)

## Tech Stack

- Python
- Ollama (Llama 3)
- Vosk (speech-to-text)
- Requests

## Project Structure

app/
├─ core/        # assistant loop + memory
├─ llm/         # LLM backends (Ollama, future APIs)
├─ stt/         # speech input
├─ tts/         # speech output
└─ main.py

## Setup

1. Clone the repo:
   git clone https://github.com/yourusername/visjar.git

2. Create virtual environment:
   python -m venv .venv

3. Install dependencies:
   pip install -r requirements.txt

4. Install Ollama:
   https://ollama.com

5. Run model:
   ollama run llama3

6. Run the app:
   python -m app.main

## Usage

- Type or speak input
- Varjis responds using local AI
- Type "exit" to quit
- Type "clear memory" to reset conversation

## Future Improvements

- Text-to-speech (voice output)
- Wake word ("Varjis")
- Smart long-term memory
- Desktop automation

## Notes

- memory.json is not included in the repo
- .env is excluded for security