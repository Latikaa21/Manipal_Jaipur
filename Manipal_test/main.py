from flask import Flask
from routes.auth import auth_blueprint
from routes.finance_ai import finance_ai_blueprint
from routes.voice import voice_blueprint
from config import Config
from db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Register blueprints (routes)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(finance_ai_blueprint, url_prefix="/finance")
    app.register_blueprint(voice_blueprint, url_prefix="/voice")

    return app
