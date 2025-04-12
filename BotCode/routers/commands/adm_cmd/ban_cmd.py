# BotCode/routers/commands/user_cmd/stats_cmd.py
# Работа с командой /stats, для получения информации о себе

from aiogram import types
from BotLibrary import CommandHandler, bot, db

# Настройки экспорта в модули
__all__ = ("ban_cmd",)

# Функция блокировки пользователя
async def ban_user(message: types.Message, *args, **kwargs) -> None:
    status = db.get_user_status(message)
    if status not in ('Пользователь', 'Забаннен'):
        # Проверка, что команда вызвана с упоминанием пользователя
        args = message.text.split()
        if len(args) != 2:
            await message.reply("Пожалуйста, укажите пользователя для бана, например: /ban @username")
            return

        # Получение упомянутого пользователя
        username = args[1]

        # Попытка получить user_id по username
        try:
            user = await bot.get_users(username)
            user_id = user.id

            # Проверка, является ли пользователь участником чата
            member = await bot.get_chat_member(message.chat.id, user_id)

            # Блокировка пользователя
            await bot.kick_chat_member(message.chat.id, user_id)
            await message.reply(f"Пользователь {username} забанен.")
        except Exception as e:
            await message.reply(f"Ошибка: {str(e)}")
    else:
        await message.reply("Вы не являетесь администратором!")


# Создание команды /ban с несколькими медиа
ban_cmd = CommandHandler(
    name="ban",
    description="Блокировка пользователя",
    keywords=["ban", "бан", "banhammer", "ифтрфььук", "ифт"],
    media="command", func=[ban_user],
)
