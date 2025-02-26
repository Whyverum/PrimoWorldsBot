# main.py
# Основной код проекта, который и соединяет в себе все его возможности

import asyncio
from BotLibrary import *
from BotCode import router as main_router
from SQLite3 import create_user_db


# Запуск основного кода
async def main():
    # Функция создания логеров и получения информации о боте
    await setup_logger()
    await bot_get_info()
    Logs.start(text=f"Начало запуска бота @{BotInfo.username}...")
    bot_info_out()

    # Автоматическое создание базы данных при отсутствии
    await create_user_db()

    # Создание пустых директорий
    await setup_directories()

    # Подключение главного маршрутизатора
    dp.include_router(main_router)

    # Нужно ли удалить веб-хук
    if Permissions.delete_webhook:
        await bot.delete_webhook()

    # Включение опроса бота
    await dp.start_polling(bot)


# Вечная загрузка бота
if __name__ == "__main__":
    asyncio.run(main())
