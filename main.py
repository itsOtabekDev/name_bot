from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from function import handle_text
# TOKEN = os.getenv()
def start_func(update, context):
    update.message.reply_text(text="Salom bu botga ism yozing bot sizga yozgan ismingizni manosini topib beradi!")
    print(update.message.text)
    print(context.bot)
    print(update.message.from_user)

updater = Updater(token="7280611441:AAFnaRxjEnoIx_PUIiLr2TeUvGmCNqLEZ9s")
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_func))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
updater.start_polling()
updater.idle()
