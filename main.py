from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from conf import token_telegram
from bot_telegram import *

app = ApplicationBuilder().token(token_telegram).build()
print('server start')
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("weather", weather))
app.run_polling()