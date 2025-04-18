# BotCode/routers/commands/user_cmd/start_cmd.py
# Работа с командой /start, для запуска бота

from BotLibrary import CommandHandler
from BotCode.keyboards import get_start_kb

# Настройки экспорта в модули
__all__ = ("start_cmd",)

# Создание команды /start с несколькими медиа
start_cmd = CommandHandler(
    name="start",
    description="Добро пожаловать!",
    keywords=["start", "старт", "cnfhn", "ыефке", "пуск", "gecr", "on"],
    keyboard=get_start_kb,
    media="photo", path_to_media=["ProjectsFiles/media/Banners/start_banner.jpg",],
    text_msg="Привет! Вот группа фото!",
)
