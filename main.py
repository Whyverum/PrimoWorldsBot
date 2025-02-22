# main.py
# Основной код проекта, который и соединяет в себе все его возможности

import asyncio
from BotLibrary import *

# Запуск основного кода
async def main():
    # Функция создания логеров и получения информации о боте
    await setup_logger()
    await bot_get_info()
    logger.bind(log_type="AEP", user="@Console").info(f"Начало запуска бота @{BotInfo.username}...")

    # Включение опроса бота
    await dp.start_polling(bot)
    await bot.delete_webhook()


# Вечная загрузка бота
if __name__ == "__main__":
    asyncio.run(main())
