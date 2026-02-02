from pathlib import Path
import os
from dotenv import load_dotenv
import telebot as bot

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

TOKEN = os.getenv("TOKEN_TELEGRAM")

if not TOKEN:
    raise ValueError("TOKEN_TELEGRAM não encontrado no .env")

bot = bot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()