from flask import Blueprint, request, jsonify
from app.voice_navigation.stt import convert_speech_to_text
from app.voice_navigation.tts import generate_speech_response

voice_bp = Blueprint("voice", __name__)

@voice_bp.route("/voice-command", methods=["POST"])
def voice_command():
    audio_data = request.files["file"]
    text_command = convert_speech_to_text(audio_data)
    return jsonify({"command": text_command})

@voice_bp.route("/text-to-speech", methods=["POST"])
def text_to_speech():
    data = request.json
    speech_audio = generate_speech_response(data["text"])
    return speech_audio
