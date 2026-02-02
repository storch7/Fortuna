import telebot
from config import TOKEN_TELEGRAM

bot = telebot.TeleBot(TOKEN_TELEGRAM, threaded=False)