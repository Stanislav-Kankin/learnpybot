import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice as ch

logging.basicConfig(filename='error_bot.log', level=logging.INFO)

hello = ['Чё каво, друже?','Здарова!','Как сам?','О, привет))','Чуваааак привет)']

def hello_user(update, context):
    update.message.reply_text(ch(hello))
    

def main():
    mybot = Updater('6539925251:AAEnOW-JHvrlzMDkavSMSHGBDmj-C2orvw0', use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', hello_user))

    logging.info('Начало рабоыт бота')
    mybot.start_polling()
    mybot.idle()
main()