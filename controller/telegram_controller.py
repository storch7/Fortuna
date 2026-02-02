from model.api.telegram_api import bot

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)