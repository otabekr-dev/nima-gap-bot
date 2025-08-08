from telegram import ChatMember, Bot, ChatInviteLink

def check_group_membership(func):
    def wrapper(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        bot: Bot = context.bot

        try:
            member = bot.get_chat_member(-1002628195498, user_id)
            # Agar foydalanuvchi kanal a'zosi bo'lmasa
            if member.status not in [ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.CREATOR]:
                update.message.reply_text(
                    f"⛔ Botdan foydalanish uchun SN01 guruhga a'zo bo‘ling."
                )
                chat_invite_link: ChatInviteLink = bot.create_chat_invite_link(-1002628195498)
                
                update.message.reply_text(chat_invite_link.invite_link)
                
                return
        except Exception as e:
            update.message.reply_text("❗ Tekshiruvda xatolik yuz berdi.")
            return

        # Agar a'zo bo'lsa - asl handlerni ishlatish
        return func(update, context, *args, **kwargs)
    return wrapper
