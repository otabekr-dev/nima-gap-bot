from config import config
from config import states
from telegram.ext import (
    Updater, 
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)
from handlers.start import start
from handlers.cancel import cancel
from handlers.register import start_register, set_name, set_gender, set_location, set_number
from handlers.profile import set_language


def main() -> None:
    updater = Updater(config.TOKEN)

    dispatcher = updater.dispatcher

    # Command Handlers
    dispatcher.add_handler(CommandHandler('start', start))

    # Message Handlers
    # dispatcher.add_handler(MessageHandler(Filters.regex("^(Bosh sahifa)$"), ))

    # Callback Query Handlers
    dispatcher.add_handler(CallbackQueryHandler(set_language, pattern='lang:'))

    # Conversation Handlers
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("^(Ro'yxatdan o'tish|Registration)$"), start_register)],
        states={
            states.NAME: [MessageHandler(Filters.text, set_name)],
            states.GENDER: [MessageHandler(Filters.text, set_gender)],
            states.LOCATION: [MessageHandler(Filters.location, set_location)],
            states.NUMBER: [MessageHandler(Filters.contact, set_number)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
