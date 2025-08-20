from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN
import handlers


def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', handlers.start))

    dispatcher.add_handler(MessageHandler(Filters.text("Buyurtmalarim"), handlers.order))
    dispatcher.add_handler(MessageHandler(Filters.text("Sozlamalar"), handlers.settings))
    dispatcher.add_handler(MessageHandler(Filters.text("Telefon raqingizni ozgartish"), handlers.contact))

    updater.start_polling()
    updater.idle()

main()
