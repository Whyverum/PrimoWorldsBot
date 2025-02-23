# BotCode/routers/commands/user_cmd/start_cmd.py
# # Работа с командой /start, для запуска бота

from BotLibrary import CommandHandler
from BotCode.keyboards import get_start_kb

# Создание команды /start с нужными параметрами
start_cmd = CommandHandler(
    name="start",
    description="Добро пожаловать!",
    keywords=["start", "старт", "запуск", "пуск", "on", "вкл", "с", "s", "ы",
              "ыефке", "cnfhn", "pfgecr", "gecr", "щт", "drk", "restart", "куыефке"],
    callbackdata="keywords",
    text_msg="Старт!",
    keyboard=get_start_kb,
)
