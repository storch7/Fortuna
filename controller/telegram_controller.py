from datetime import datetime
from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)

from model.api.telegram_api import bot

# ====== ESTADOS DO FLUXO ======
WAIT_DESC, WAIT_VALUE, WAIT_DATE, CONFIRM = range(4)


# ====== MENU ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()

    await update.message.reply_text(
        "👋 Olá! Eu sou seu bot financeiro.\n\n"
        "O que você deseja fazer agora?\n\n"
        "📌 /inserir — Registrar uma compra/lançamento\n"
        "❓ /ajuda — Ver comandos disponíveis\n"
        "🛑 /cancel — Cancelar operação atual\n"
    )


async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *Ajuda*\n\n"
        "Comandos disponíveis:\n"
        "📌 /inserir — Registrar um lançamento\n"
        "🛑 /cancel — Cancelar fluxo atual\n"
        "🏠 /start — Voltar ao menu inicial\n",
        parse_mode="Markdown"
    )


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text(
        "🛑 Operação cancelada.\n\n"
        "Você pode voltar ao menu com /start"
    )
    return ConversationHandler.END


# ====== FLUXO INSERIR ======
async def inserir_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["lancamento"] = {}

    await update.message.reply_text(
        "📌 *Inserir lançamento*\n\n"
        "Me diga a *descrição*.\n"
        "Ex: `Uber`, `Mercado`, `iFood`, `Aluguel`",
        parse_mode="Markdown"
    )
    return WAIT_DESC


async def inserir_desc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    desc = update.message.text.strip()
    context.user_data["lancamento"]["descricao"] = desc

    await update.message.reply_text(
        "Boa! Agora me diga o *valor*.\n\n"
        "Exemplos válidos:\n"
        "`35.90`\n"
        "`120`\n"
        "`-50` (se for estorno/entrada negativa)\n",
        parse_mode="Markdown"
    )
    return WAIT_VALUE


async def inserir_value(update: Update, context: ContextTypes.DEFAULT_TYPE):
    raw = update.message.text.strip().replace(",", ".")

    try:
        value = float(raw)
    except ValueError:
        await update.message.reply_text(
            "❌ Não consegui entender esse valor.\n"
            "Digite somente números.\n\n"
            "Ex: `35.90`",
            parse_mode="Markdown"
        )
        return WAIT_VALUE

    context.user_data["lancamento"]["valor"] = value

    await update.message.reply_text(
        "Perfeito.\n\n"
        "📅 Agora me diga a *data*.\n\n"
        "Você pode digitar:\n"
        "✅ `hoje`\n"
        "ou uma data no formato: `DD/MM/AAAA`\n\n"
        "Ex: `03/02/2026`",
        parse_mode="Markdown"
    )
    return WAIT_DATE


async def inserir_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    raw = update.message.text.strip().lower()

    if raw == "hoje":
        date = datetime.now().date()
    else:
        try:
            date = datetime.strptime(raw, "%d/%m/%Y").date()
        except ValueError:
            await update.message.reply_text(
                "❌ Data inválida.\n\n"
                "Use `hoje` ou `DD/MM/AAAA`.\n"
                "Ex: `03/02/2026`",
                parse_mode="Markdown"
            )
            return WAIT_DATE

    context.user_data["lancamento"]["data"] = date.isoformat()

    lanc = context.user_data["lancamento"]
    desc = lanc["descricao"]
    valor = lanc["valor"]
    data = lanc["data"]

    await update.message.reply_text(
        "🔎 *Confirme os dados:*\n\n"
        f"📝 Descrição: *{desc}*\n"
        f"💰 Valor: *{valor:.2f}*\n"
        f"📅 Data: *{data}*\n\n"
        "Digite:\n"
        "✅ `confirmar`\n"
        "ou ❌ `cancelar`",
        parse_mode="Markdown"
    )
    return CONFIRM


async def inserir_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    raw = update.message.text.strip().lower()

    if raw not in ["confirmar", "cancelar"]:
        await update.message.reply_text(
            "Responda com `confirmar` ou `cancelar`.",
            parse_mode="Markdown"
        )
        return CONFIRM

    if raw == "cancelar":
        context.user_data.clear()
        await update.message.reply_text(
            "❌ Lançamento cancelado.\n\n"
            "Volte ao menu com /start"
        )
        return ConversationHandler.END

    # Aqui futuramente você chama o Notion
    lanc = context.user_data["lancamento"]

    context.user_data.clear()
    await update.message.reply_text(
        "✅ Lançamento registrado (simulação).\n\n"
        "⚠️ Por enquanto eu ainda não enviei pro Notion.\n"
        "Quando você plugar a integração, aqui será o envio.\n\n"
        "Volte ao menu com /start"
    )
    return ConversationHandler.END


# ====== RUN ======
def run():
    print("🚀 Bot iniciando polling...")

    inserir_conv = ConversationHandler(
        entry_points=[CommandHandler("inserir", inserir_start)],
        states={
            WAIT_DESC: [MessageHandler(filters.TEXT & ~filters.COMMAND, inserir_desc)],
            WAIT_VALUE: [MessageHandler(filters.TEXT & ~filters.COMMAND, inserir_value)],
            WAIT_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, inserir_date)],
            CONFIRM: [MessageHandler(filters.TEXT & ~filters.COMMAND, inserir_confirm)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("ajuda", ajuda))
    bot.add_handler(CommandHandler("cancel", cancel))
    bot.add_handler(inserir_conv)

    bot.run_polling()
