# BotCode/routers/commands/user_cmd/start_cmd.py
# # Работа с командой /start, для запуска бота

from .user_cmd_class import CommandHandler

# Создание команды /start с нужными параметрами
start_cmd = CommandHandler(
    name="start",
    description="Запустить бота",
    keywords=["start", "старт", "запуск", "пуск", "on", "вкл", "с", "s", "ы",
              "ыефке", "cnfhn", "pfgecr", "gecr", "щт", "drk", "restart", "куыефке"],
    text_msg="Старт!",
)
