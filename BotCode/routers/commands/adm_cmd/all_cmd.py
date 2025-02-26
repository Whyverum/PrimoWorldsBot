# BotCode/routers/commands/adm_cmd/all_cmd.py
# Работа с командой /all, для всеобщего призыва

from BotLibrary import CommandHandler

# Настройки экспорта в модули
__all__ = ("all_cmd",)

# Создание команды /start с несколькими медиа
all_cmd = CommandHandler(
    name="all",
    description="Всеобщий призыв",
    keywords=["all", "фдд", "@all"],
    callbackdata=["keywords"],
    text_msg="ТЕСТ! НЕ РАБОТАЕТ!",
)
