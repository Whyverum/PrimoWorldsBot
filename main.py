# main.py
# Основной код проекта, который и соединяет в себе все его возможности

from BotLibrary import *
from ProjectsFiles import Permissions
from BotCode import router as main_routers

# Запуск основного кода
async def main() -> None:
    # Запуск логеров
    Logs.setup()

    # Получение информации о боте
    await BotInfo.info()

    # Вывод сообщение о запуске
    Logs.start(text=f"Начало запуска бота @{BotInfo.username}...")

    # Создание пустых директорий
    await Directory.setup()

    # Нужно ли удалить веб-хук
    if Permissions.delete_webhook:
        await bot.delete_webhook()

    # Установка необходимых прав
    await BotRights.all(bot)
    Logs.console()

    # Подключение главного маршрутизатора
    dp.include_router(main_routers)

    # Включение опроса бота
    await dp.start_polling(bot)

# Вечная загрузка бота
if __name__ == "__main__":
    from asyncio import run
    run(main())
