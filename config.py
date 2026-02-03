import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")
TOKEN_NOTION = os.getenv("TOKEN_NOTION")

if not TOKEN_TELEGRAM:
    raise RuntimeError("TOKEN_TELEGRAM não definido no .env")

if not TOKEN_NOTION:
    raise RuntimeError("TOKEN_NOTION não definido no .env")