# BotCode/routers/handlers/leave_member_notification.py
# Вывод уведомления о покидании участника

from aiogram import Router, types
from aiogram.filters import ChatMemberUpdatedFilter, LEAVE_TRANSITION
from BotLibrary import Logs

# Создание роутера и настройка экспорта в модули
__all__ = ("router",)
router = Router(name="leave_member_notification_router")


# Роутер по покиданию участников чата
@router.chat_member(ChatMemberUpdatedFilter(LEAVE_TRANSITION))
async def leave_member_handler(event: types.ChatMemberUpdated) -> None:
    chat_id = event.chat.id
    leaving_user = event.old_chat_member.user

    # Привязка пользователя по ссылке
    leaving_user_link = f"<b><a href=\"tg://user?id={leaving_user.id}\">{leaving_user.full_name}</a></b>"

    # Сообщение с упоминанием администраторов
    farewell_text = (f"Пользователь {leaving_user_link} покинул чат. "
                     f"Мы будем скучать по тебе! 😔\n"
                     f"Надеемся, ты вернёшься, когда захочешь снова пообщаться с нами!")

    Logs.debug(log_type="LEAVE", user=f"@{leaving_user.username or leaving_user.id}", text="Участник покинул чат!")
    await event.bot.send_message(chat_id, farewell_text, parse_mode="HTML")
