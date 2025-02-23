# BotLibrary/analitics/find_username.py
# Нахождение юзернейма пользователя по id    (в разработке)

from loguru import logger
from BotLibrary.library.bots import bot

# Настройка экспорта
__all__ = ("get_user_id_by_username",)
type_messages = "ID_USERNAME"


# Получение ID пользователя по юзернейму    (в разработке)
async def get_user_id_by_username(chat_id, username):
    try:
        user = await bot.get_chat_member_by_username(chat_id, username)
        if user:
            return user.user.id
        else:
            return None

    # Проверка на ошибку и ее логирование  (в разработке)
    except Exception as e:
        text_error = f"Ошибка при получении ID пользователя: {e}"
        logger.bind(custom_variable="IDS", user_var=type_messages).error(text_error)
        return text_error
