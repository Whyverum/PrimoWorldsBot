# main.py
# Основной код проекта, который и соединяет в себе все его возможности

import asyncio
from BotLibrary import *
from BotCode import router as main_router

# Запуск основного кода
async def main():
    # Функция установки
    await setup()

    # Подключение главного маршрутизатора
    dp.include_router(main_router)

    # Включение опроса бота
    await dp.start_polling(bot)

# Вечная загрузка бота
if __name__ == "__main__":
    asyncio.run(main())
