# BotCode/routers/commands/user_cmd/help_cmd.py
# Работа с командой /help, для вывода помощи пользователю

from BotLibrary import CommandHandler
from BotCode.keyboards import get_help_kb

# Настройки экспорта в модули
__all__ = ("help_cmd",)

# Создание команды /help с нужными параметрами
help_cmd = CommandHandler(
    name="help",
    description="Получить помощь",
    keywords=["help", "info", "помощь", "инфо", "информация", "рудз", "штащ", "byaj", "gjvjom", "byajhvfwbz"],
    callbackdata="keywords",
    keyboard=get_help_kb,
    text_msg="Привет! Это команда помощи. Тут ты можешь узнать, как пользоваться ботом.",
    #media="", path_to_media=""
)
