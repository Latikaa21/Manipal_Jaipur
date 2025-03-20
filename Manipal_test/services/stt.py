import whisper
import requests
from config import Config

# Load Whisper Model
stt_model = whisper.load_model("medium", device="cpu")

def transcribe_audio(audio_path):
    """Convert speech to text using Whisper or Deepgram API."""
    result = stt_model.transcribe(audio_path)
    return result["text"]
