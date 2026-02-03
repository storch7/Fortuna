from telegram.ext import ApplicationBuilder
from config import TOKEN_TELEGRAM

#bot = telebot.TeleBot(TOKEN_TELEGRAM, threaded=False)
bot = ApplicationBuilder().token(TOKEN_TELEGRAM).build()