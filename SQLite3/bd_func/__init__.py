# SQLite3/bd_func/__init__.py
# Инициализация модуля bd_func, для функция с БД

from aiogram import types
from BotLibrary.validators import username
from ProjectsFiles import Permissions

from .bd_add_user import *
from .bd_get_user import *
from .bd_update_user import *
from .bd_update_user_msg import *
from .bd_user_create import *
from .status_user import *


# Основная обработка SQL
async def base_sql(message: types.Message):
    tg_id = message.from_user.id
    usernames = username(message)
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    if Permissions.sql_user:
        await add_user(tg_id, usernames, first_name, last_name, role="", status="active", user="user")
        await update_user(tg_id=tg_id, first_name=first_name, last_name=last_name)
        await update_user_messages(message=message)
