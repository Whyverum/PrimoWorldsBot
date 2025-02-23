# BotCode/routers/commands/user_cmd/help_cmd.py
# Работа с командой /help, для вывода помощи пользователю

from BotLibrary import CommandHandler
from BotCode.keyboards import get_start_kb


# Создание команды /help с нужными параметрами
help_cmd = CommandHandler(
    name="help",
    description="Получить помощь",
    keywords=["help", "info", "помощь", "инфо", "информация", "рудз", "штащ", "byaj", "gjvjom", "byajhvfwbz"],
    callbackdata="keywords",
    keyboard=get_start_kb,
    text_msg="Привет! Это команда помощи. Тут ты можешь узнать, как пользоваться ботом.",
    media="gif", path_to_media="https://t.me/c/2442589033/74653"
)
