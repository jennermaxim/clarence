from dotenv import load_dotenv
import os

from dotenv import load_dotenv

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your_secure_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///medical_records.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OAUTH2_CLIENT_ID = 'your_client_id'
    OAUTH2_CLIENT_SECRET = 'your_client_secret'
    OAUTH2_AUTHORIZE_URL = 'https://auth.example.com/authorize'
    OAUTH2_TOKEN_URL = 'https://auth.example.com/token'
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY') or 'encryption_key_32_bytes'
