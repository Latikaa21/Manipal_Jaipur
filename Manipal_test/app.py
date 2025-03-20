from flask import Flask
from config import Config
from db import db
from routes.auth import auth_bp
from routes.voice import voice_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(voice_bp, url_prefix="/voice")

if __name__ == "__main__":
    app.run(debug=True)
