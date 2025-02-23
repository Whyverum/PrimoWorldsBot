# BotCode/routers/old_files/regular_handlers.py
# Регулярная функция, выдает тебе сообщение на код при сообщении с числами

from aiogram import F, types, Router
from magic_filter import RegexpMode
from re import Match

from BotLibrary import logginger
import configs

# Настройка экспорта модулей и роутера
__all__ = ("router",)
router = Router(name="regular_handlers")


# Хэндлер на циферный код (регулярная функция)
@router.message(
    F.from_user.id.in_(configs.ListId.adm_list_id),
    F.text.regexp(r"(\d+)", mode=RegexpMode.MATCH).as_("code"),
)
async def handle_code(message: types.Message, code: Match[str]):
    # Вывод сообщения
    text = f"Ваш код: {code.group()}"
    await message.reply(text)

    # Включение логирования в файл
    await logginger(message)

    return text
