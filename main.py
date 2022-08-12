# телеграм-бот для работы со справочником телефонов

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5429784803:AAG3_FbbEOZMpiGlutRqsG-9rr5QfHAREWY").build()
print('server start')
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("add", add_command))
app.add_handler(CommandHandler("exp", exp_command))
app.add_handler(CommandHandler("imp", imp_command))
app.add_handler(CommandHandler("search", search_command))

app.run_polling()