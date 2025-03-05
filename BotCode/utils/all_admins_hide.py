# BotCode/utils/all_admins_hide.py
# Составления листа администраторов (для скрытого отправления)

from aiogram import types
from aiogram.utils import markdown
from BotLibrary import bot

# Настройки экспорта в модули
__all__ = ("hidden_admins_message",)


# Функция составления словаря администраторов
async def hidden_admins_message(message: types.Message = None, chat_id: int = None, text: str = "", msg: bool = True, *args):
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
