from aiogram import Router, types
from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION

from BotLibrary import Logs
from ProjectsFiles import BotEdit

# Создание роутера и настройка экспорта в модули
__all__ = ("router",)
router = Router(name="new_member_notification_router")


# Роутер по новым участникам чата
@router.chat_member(ChatMemberUpdatedFilter(JOIN_TRANSITION))
async def new_member_handler(event: types.ChatMemberUpdated):
    chat_id = event.chat.id
    new_user = event.new_chat_member.user
    admins = await event.bot.get_chat_administrators(chat_id)

    # Формируем список упоминаний администраторов
    admin_mentions = []
    for admin in admins:
        if admin.user.is_bot:
            continue
        admin_mentions.append(
            f"@{admin.user.username}" if admin.user.username else f"<a href=\"tg://user?id={admin.user.id}\">{admin.user.full_name}</a>")

    admins_text = ", ".join(admin_mentions) if admin_mentions else "Нет администраторов для упоминания"

    # Привязка пользователя по ссылке
    new_user_link = f"<b><a href=\"tg://user?id={new_user.id}\">{new_user.full_name}</a></b>"

    # Сообщение с упоминанием администраторов
    welcome_text = (f"Приветствуем тебя, {new_user_link}! 👋\n"
                    f"Мы рады тебя приветствовать в проекте <b>{BotEdit.project_name}</b> "
                    f"Надеемся, что вы сможете найти здесь друзей и провести весело время с нами!\n"
                    f"А пока уведомлю участников чата: {admins_text}")

    Logs.debug(log_type="NEW", user=f"@{new_user.username or new_user.id}", text="Новый участник чата!")
    await event.bot.send_message(chat_id, welcome_text, parse_mode="HTML")
