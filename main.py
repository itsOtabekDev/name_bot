from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from function import handle_text
import os
TOKEN = os.getenv("TOKEN")
def start_func(update, context):
    update.message.reply_text(text="Salom bu botga ism yozing bot sizga yozgan ismingizni manosini topib beradi!")
    print(update.message.text)
    print(context.bot)
    print(update.message.from_user)

updater = Updater(token=f"{TOKEN}")
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_func))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
updater.start_polling()
updater.idle()
