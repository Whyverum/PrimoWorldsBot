# BotCode/routers/commands/user_cmd/help_cmd.py
# Работа с командой /help, для вывода помощи пользователю

from .user_cmd_class import CommandHandler

# Создание команды /help с нужными параметрами
help_cmd = CommandHandler(
    name="help",
    description="Получить помощь",
    keywords=["help", "info", "помощь", "инфо", "информация", "рудз", "штащ", "byaj", "gjvjom", "byajhvfwbz"],
    text_msg="Привет! Это команда помощи. Тут ты можешь узнать, как пользоваться ботом.",
)
