import os
from dotenv import load_dotenv
import telebot as bot

load_dotenv()

bot = bot.TeleBot(os.getenv('TOKEN_TELEGRAM'))

print(bot)