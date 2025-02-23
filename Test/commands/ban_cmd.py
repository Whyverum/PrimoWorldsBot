# BotCode/routers/commands/admin_cmd/ban_cmd.py
# Работа с админ-командой /ban, для блокировки пользователей  (в разработке)
# Проверка на наличие блокировки пользователя в боте


from aiogram import Router, types
from aiogram.filters import Command
from BotLibrary import *

# Создание роутера и настройка экспорта
__all__ = ("router", "banned_user", "ban_user_by_username",)
router = Router(name="ban_router")
command_text = "BAN"


# Функция проверки блокировки пользователя в боте
@router.message(lambda message: message.from_user.id in ListId.ban_list_id)
async def banned_user(message: types_msg.Message):
    try:
        # Вывод сообщения пользователю
        chat_id = await find_chat_id(message)
        text = (f"{TextDecorator.RED}Получено сообщение от забанненго пользователя"
                f" из ({chat_id}) : {message.text}{TextDecorator.RESET_DECORATOR}")
        await message.answer(f"Вы были забаннены в боте @{BotInfo.username}!")

        # Активация логгера
        await cmd_logginger(message, command_text, text)

        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, command_text, e)
        return text_error


# Обработчик команды /ban
@router.message(Command("ban", "ифт", "бан", ",fy", prefix=BotEdit.prefixs, ignore_case=True))
async def ban_user_by_username(message: types_msg.Message):
    try:
        text = f"использовал(а) команду /{command_text.lower()}"

        # Получаем аргументы команды
        args = message.get_args()  # Вернет все, что идет после /ban

        # Проверка на наличие аргумента
        if not args:
            text = f"Пожалуйста, укажите ID или имя пользователя для бана. Пример: /ban 123456"
            await message.reply(text)
            return text

        # Вывод сообщения пользователю
        await message.reply(text=f"Вы попытались забанить, обидно да?")

        # Активация логгера
        await cmd_logginger(message, command_text, text)

        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, command_text, e)
        return text_error
