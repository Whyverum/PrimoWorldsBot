# BotCode/routers/commands/adm_cmd/all_cmd.py
#

from BotCode.utils import hidden_admins_message
from BotLibrary import CommandHandler

# Настройки экспорта в модули
__all__ = ("all_cmd",)

# Текст, который вы хотите передать по умолчанию
custom_text = "<b>Важное уведомление!</b>"

# Создание команды /all с несколькими медиа
all_cmd = CommandHandler(
    name="all",
    description="Всеобщий призыв",
    keywords=["all", "фдд", "@all"],
    callbackdata=["keywords"],
    media="command",
    func=[lambda message, *args: hidden_admins_message(message, msg=False, text=message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else custom_text)],
)
