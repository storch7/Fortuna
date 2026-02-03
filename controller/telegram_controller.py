from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from model.api.telegram_api import bot


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Howdy, how are you doing?")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


def run():
    print("🚀 Bot iniciando polling...")
    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    bot.run_polling()