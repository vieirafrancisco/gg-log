import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgres://user:password@localhost:5432/database')
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
