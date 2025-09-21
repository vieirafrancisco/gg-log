import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgres://user:password@localhost:5432/database')
