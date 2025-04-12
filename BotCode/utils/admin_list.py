# BotCode/utils/admin_lists.py
# Составления листа администраторов

from aiogram.types import Message
from BotLibrary import bot
from ProjectsFiles import BotVar

# Настройки экспорта в модули
__all__ = ("admin_lists",)

async def admin_lists(chat_id: int = None, message: Message = None) -> str:
    """
    Функция составления словаря администраторов.

    :param message: Объект сообщения от пользователя.
    :param chat_id: ID-чата в котором будет проводиться работа.
    :return: Строка с юзерами администрации.
    """
    chat_id = chat_id if isinstance(chat_id, int) else message.chat.id
    admins = await bot.get_chat_administrators(chat_id)

    # Формируем список упоминаний администраторов
    admin_mentions = []
    for admin in admins:
        if admin.user.is_bot:
            continue
        if BotVar.parse_mode == "HTML":
            admin_mentions.append(
            f"@{admin.user.username}" if admin.user.username else f"<a href=\"tg://user?id={admin.user.id}\">{admin.user.full_name}</a>")
        elif BotVar.parse_mode == "MarkdownV2":
            admin_mentions.append(
            f"@{admin.user.username}" if admin.user.username else f"[{admin.user.full_name}](tg://user?id={admin.user.id})")
    admins_text = ", ".join(admin_mentions) if admin_mentions else "Нет администраторов"
    return admins_text
