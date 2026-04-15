import json
import queue
import sounddevice as sd
from vosk import KaldiRecognizer, Model
import os

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../models/vosk-model-small-en-us-0.15"
)
MODEL_PATH = os.path.abspath(MODEL_PATH)
SAMPLE_RATE = 16000
audio_queue: queue.Queue[bytes] = queue.Queue()
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

def callback(indata, frames, time, status) -> None:
    if status:
        print(status)
    audio_queue.put(bytes(indata))

def listen() -> str:
    print("Listening... Speak now.")
    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback,
        device=3
    ):
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip()

                if text:
                    print(f"You: {text}")
                    return text