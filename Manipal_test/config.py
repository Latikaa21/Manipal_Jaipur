import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_URL")
    MONGO_URI = os.getenv("MONGO_URI")
    CORS_HEADERS = "Content-Type"
