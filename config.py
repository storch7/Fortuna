from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent

#load_dotenv(BASE_DIR / ".env.exemple")
load_dotenv(BASE_DIR / ".env")

TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")

if not TOKEN_TELEGRAM:
    raise RuntimeError("TOKEN_TELEGRAM não definido no .env")