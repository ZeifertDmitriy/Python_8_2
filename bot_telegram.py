import bot_weather
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from conf import token_weather

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        city = update.message.text.split()
        res = bot_weather.get_weather(city[1], token_weather)
        await update.message.reply_text(res) 
    except Exception as e:
        update.bot.reply_to(update.message, e)