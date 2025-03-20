from TTS.api import TTS
import simpleaudio as sa
from config import Config

# Load TTS Model
tts_model = TTS(Config.TTS_MODEL_PATH).to("cpu")

def text_to_speech(text, file_path="output.wav"):
    """Convert text to speech and play it."""
    tts_model.tts_to_file(text=text, file_path=file_path)
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    wave_obj.play()
