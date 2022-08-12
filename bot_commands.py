from tokenize import Token
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import telebot

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/help\n/add\n/exp\n/imp\n/search')

async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        stroka = update.message.text.split()
        with open('data\spr.csv', 'a', encoding='utf-8') as file:
            file.write('{},{}\n'.format(stroka[1], stroka[2]))
        await update.message.reply_text(f'Абонент {stroka[1]} с номером телефона {stroka[2]} внесен в телефонный справочник.') 
    except Exception as e:
        update.bot.reply_to(update.message, e)

async def exp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    try:
        await context.bot.send_document(chat_id,open('data\spr.csv', 'rb'))
    except Exception as e:
        update.bot.reply_to(update.message, e)

async def imp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    file_path = '/data/imp/'
    print('file_id')
    file_id = await context.bot.get_file(update.message.document.file_id)
    print(file_id)
    #f_id = update.message.document.file_id
    #file_info = await context.bot.get_file(f_id)
    # downloaded_file = context.bot.download_file(file_info.file_path)
    downloaded_file = await context.bot.download_file(file_id, file_path)

#     src = file_path + update.message.document.file_name
#     print(src)
#     with open(src, 'wb') as new_file:
#         new_file.write(downloaded_file)    
    

#     # src = 'C:/Python/Project/tg_bot/files/received/' + message.document.file_name;
#     # with open(src, 'wb') as new_file:
#     #     new_file.write(downloaded_file)


async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.split()
    msg = msg[1]
    spisok = []
    with open('data\spr.csv', 'r', encoding='utf-8') as file:
        for line in file:
            spisok = line
            spisok = spisok [:len(spisok)-1]
            l = spisok.find(msg)
            if l >= 0:
                spisok = spisok.split(',')
                await update.message.reply_text(f'Абонент {spisok[0]}, телефон {spisok[1]}')