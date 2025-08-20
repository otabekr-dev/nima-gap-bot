from telegram import Update, ParseMode, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    user = update.effective_user

    update.message.reply_text(
        text=f'Assalomu alaykum <b>{user.first_name}<b>',
        parse_mode=ParseMode.HTML,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton("Buyurtmalar berish", web_app=WebAppInfo("https://kun.uz"))
                ],
                [KeyboardButton("Buyurtmalarim"), KeyboardButton("Sozlamalar")],
                [KeyboardButton("Biz haqimizda"), KeyboardButton("Fikr qoldirish")],
                [
                    KeyboardButton("Contact Yuborish", request_contact=True),
                    KeyboardButton("Lokatsiya Yuborish", request_location=True)
                ]
            ],
            resize_keyboard=True,
            # one_time_keyboard=True
        )
    )


def order(update: Update, context: CallbackContext):
    update.message.reply_text("Sizda hali birorta ham buyurtma yo`q")

def settings(update: Update, context: CallbackContext):
    update.message.reply_text(
        "⚙️ Sozlamalar",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Tilni o'zgartish")],
                [KeyboardButton("Telefon raqingizni ozgartish")],
                [KeyboardButton("Orqaga")],
            ]
        ),
        reply_to_message_id=update.message.message_id
    )


def contact(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Telefon raqamni ozgartish",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Mening raqamim", request_contact=True)],
                [KeyboardButton("Orqaga")],
            ]
        )
    )


def back(update: Update, context: CallbackContext):
    start(update, context)


def set_language(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Tilni tanlang",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton("Uzbek", callback_data="language:uz")],
                [InlineKeyboardButton("English", callback_data="language:en")],
                [InlineKeyboardButton("kanalga azo boling", url="https://www.youtube.com/@nmagap")]
            ]
        )
    )


def choose_language(update: Update, context: CallbackContext):
    data = update.callback_query.data

    langs = {
        'uz': "O'zbek",
        'en': "ingliz"
    }

    _, lan = data.split(":")

    update.callback_query.message.reply_text(f"siz {langs[lan]} tilini tanladingiz")