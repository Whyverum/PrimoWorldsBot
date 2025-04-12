# BotCode/utils/all_admins_hide.py
# Составления листа администраторов (для скрытого отправления)

from aiogram import types
from aiogram.utils import markdown
from BotLibrary import bot

# Настройки экспорта в модули
__all__ = ("hidden_admins_message",)

async def hidden_admins_message(message: types.Message = None,
                                chat_id: int = None,
                                text: str = "",
                                msg: bool = True, *args) -> str | None:
    """
    Формирует скрытые ссылки на администраторов чата в Markdown-разметке.

    :param message: Объект сообщения от пользователя (если chat_id не указан, ID чата берется из него).
    :param chat_id: ID чата, в котором нужно получить список администраторов (если не указан, берется из message).
    :param text: Дополнительный текст, который будет добавлен к результату.
    :param msg: Определяет, возвращать ли результат (True) или отправлять его в чат (False).
    :param args: Дополнительные аргументы (не используются, оставлены для совместимости с шаблоном).
    :return: Строка со скрытыми ссылками на администраторов и добавленным текстом (если msg=True), иначе None.
    """
    chat_id = chat_id if isinstance(chat_id, int) else message.chat.id
    admins = await bot.get_chat_administrators(chat_id)

    hidden_links = "".join(
        markdown.hide_link(f"tg://user?id={admin.user.id}")
        for admin in admins if not admin.user.is_bot
    )

    result = f"{hidden_links}{text}"
    if msg:
        return result
    else:
        await message.answer(result)
