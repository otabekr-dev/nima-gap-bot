from telegram import Update
from telegram.ext import CallbackContext
from services import db
from middleware.check_chat_member import check_group_membership


@check_group_membership
def set_language(update: Update, context: CallbackContext):
    user = update.effective_user
    callback_data = update.callback_query.data

    _, lang = callback_data.split(":")

    db.update_user(user.id, {'lang': lang})

    context.user_data['lang'] = lang

    if lang == 'uz':
        text = "O'zbek tili tanlandi"
    else:
        text = "English is selected"

    update.callback_query.answer(text, show_alert=True)
