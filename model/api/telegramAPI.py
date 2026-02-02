import telebot
from config import TOKEN_TELEGRAM

class TelegramAPI:
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN_TELEGRAM)

    def send_message(self, chat_id, text):
        self.bot.send_message(chat_id, text)

    def reply(self, message, text):
        self.bot.reply_to(message, text)

    def start_polling(self):
        self.bot.infinity_polling()