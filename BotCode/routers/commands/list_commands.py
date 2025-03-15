# BotCode/routers/commands/list_commands.py
# Создание списка команд для бота

from aiogram import Router, types
from aiogram.filters import Command
from BotLibrary import *

from .user_cmd.start_cmd import start_cmd
from .user_cmd.help_cmd import help_cmd

# Создание роутера и настройка экспорта модулей
__all__ = ("router", "set_commands")
router = Router(name="list_cmd_routers")

# Список ключевых слов для команды "setcommands"
secret_keywords = ["setcommands", "setcommand", "ыуесщььфтвы", "ыуесщььфтв",
                   "setcmd", "setcmds", "ыуесьв",]


# Хэндлер на команду /setcommands для использования в чате
@router.message(
    #F.from_user.id.func(lambda user_id: str(user_id) in DataID.important.keys()),
                Command(*secret_keywords, prefix=BotVar.prefix, ignore_case=True))
@router.message(
    #F.from_user.id.func(lambda user_id: str(user_id) in DataID.important.keys()),
                F.text.lower().in_(secret_keywords))
async def set_commands() -> None:
    bot_commands = [
        types.BotCommand(command=start_cmd.name, description=start_cmd.description),
        types.BotCommand(command=help_cmd.name, description=help_cmd.description),
    ]
    await bot.set_my_commands(bot_commands)