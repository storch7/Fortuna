from fastapi import FastAPI, Request
from model.api.telegram_api import bot

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    bot.process_new_updates([bot.types.Update.de_json(update)])
    return {"ok": True}