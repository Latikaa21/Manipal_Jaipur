import requests
import json
from config import Config

MODEL = "mistralai/mistral-7b-instruct:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def get_ai_response(user_text):
    """Get AI response from OpenRouter (Mistral)."""
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": user_text}],
        "max_tokens": 1000,
        "temperature": 0.7,
    }

    headers = {
        "Authorization": f"Bearer {Config.OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"].get("content", "No response")
    else:
        return f"Error: {response.status_code}"
