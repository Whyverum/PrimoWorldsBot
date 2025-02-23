# BotCode/routers/commands/admin_cmd/send_to_user.py
# Работа с админ-командой /send, для отправки конкретного сообщения пользователю  (в разработке)

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *

# Создание роутера и настройка экспорта
__all__ = ("router", "send_message",)
router = Router(name="send_router")
command_text = "Send"


# Обработчик команды /send для отправки сообщения определенному пользователю    (в разработке)
@router.message(F.from_user.id.in_(ListId.important),
                Command("send", "отправить", "отправ", "s", "ыутв", "jnghfdbnm", "jnghfd",
                        prefix=BotEdit.prefixs, ignore_case=True))
async def send_message(message: types_msg.Message):
    try:
        if message.chat.id in ListId.adm_list_id:
            text = f"использовал(а) команду /{command_text.lower()}"

            # Разбиваем сообщение на аргументы
            args = message.text.split()

            # Проверка на правильность команды /send
            if len(args) < 3:
                texts = "Некорректный формат команды. Используйте: /send <user_id> <текст>"
                await message.reply(texts)
                return texts

            # Получаем user_id и текст сообщения
            user_id = int(args[1])
            text_send = ' '.join(args[2:])

            # Отправляем сообщение пользователю
            await bot.send_message(chat_id=user_id, text=text_send)

            # Логирование
            user_id = find_imp_id(user_id)
            await cmd_logginger(message, command_text, text)

            # Логирование и отчет об отправке
            await message.reply(f"Сообщение успешно отправлено пользователю с ID {user_id}")
            return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, command_text, e)
        return text_error

    # Проверка заблокирован ли бот для пользователя
    # except exceptions.BotBlocked:
    #     await message.answer("Пользователь заблокировал бота")
    #     except aiogram.utils.exceptions.ChatNotFound:
    #     await message.answer("Чат с пользователем не найден")
    # except exceptions.RetryAfter as e:
    #     await asyncio.sleep(e.timeout)
    #     return await send_message(message)
    # except exceptions.UserDeactivated:
    #     await message.answer("Пользователь деактивирован")
    # except exceptions.TelegramAPIError:
    #     await message.answer("Произошла ошибка при отправке сообщения")
    # except:
    #     return
