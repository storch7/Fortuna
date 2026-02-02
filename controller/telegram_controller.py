from model.api.telegramAPI import TelegramAPI

telegram_api = TelegramAPI()
bot = telegram_api.bot


@bot.message_handler(commands=["start"])
def start(message):
    telegram_api.reply(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo(message):
    telegram_api.reply(message, message.text)


def run():
    print("🚀 Bot iniciando polling...")
    telegram_api.start_polling()