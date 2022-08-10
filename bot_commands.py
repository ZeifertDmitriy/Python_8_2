from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/Hello\n/add\n/exp\n/imp\n/search')

async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stroka = update.message.text.split()
    with open('data\spr.csv', 'a', encoding='utf-8') as file:
        file.write('{},{}\n'.format(stroka[1], stroka[2]))
    await update.message.reply_text(f'Абонент {stroka[1]} с номером телефона {stroka[2]} внесен в телефонный справочник.') 

# async def exp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     with open('data\spr.csv', 'r', encoding='utf-8') as file:
#         f = file.read()
#         #chat_id='5056254761'
#         await update.message.sendDocument('data\spr.csv')

# async def exp_command(chat_id='5056254761'):
#     files = {'photo': open('data\spr.csv', 'rb')}
#     URL = 'https://api.telegram.org/bot'
#     requests.post(f'{URL}"5429784803:AAG3_FbbEOZMpiGlutRqsG-9rr5QfHAREWY"/sendPhoto?chat_id={chat_id}', files=files)



# async def imp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

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