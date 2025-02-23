import sys
import customtkinter as ctk
import asyncio
import threading

# Ваши настройки и модули
from BotLibrary import *
from BotCode.routers import router as main_router
from BotCode.routers import set_commands


# Класс для перенаправления стандартного вывода в текстовое поле
class Logger:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert("end", message)
        self.text_widget.see("end")  # Прокрутка к последнему сообщению

    def flush(self):
        pass


# Основная функция для запуска бота
async def main_bot():
    just_fix_windows_console()  # Подключение ANSI в Windows CMD
    dp.include_router(main_router)  # Подключение главного роутера

    await set_all()  # Установка настроек бота
    await set_commands()  # Установка команд бота
    await bot_get_info()  # Получение информации о боте

    # Логирование в консоль и текстовое поле
    logger.add(sys.stderr, colorize=True, format=logs_text, level="INFO")
    logger.info(f"Начало запуска бота @{BotInfo.username}...")

    bot_info_out()  # Включение опроса бота
    await dp.start_polling(bot)  # Запуск бота


# Класс графического интерфейса
class BotConsoleWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.title("Bot Console")
        self.geometry("800x600")

        # Создание текстового поля для логов
        self.log_text = ctk.CTkTextbox(self, wrap="word", width=780, height=500)
        self.log_text.pack(padx=10, pady=10)

        # Перенаправление вывода в текстовое поле
        sys.stdout = Logger(self.log_text)
        sys.stderr = Logger(self.log_text)

        # Кнопка запуска бота
        self.start_button = ctk.CTkButton(self, text="Запустить бота", command=self.start_bot)
        self.start_button.pack(pady=10)

    def start_bot(self):
        self.start_button.configure(state="disabled")  # Отключить кнопку
        threading.Thread(target=self.run_bot, daemon=True).start()

    def run_bot(self):
        asyncio.run(main_bot())
        self.start_button.configure(state="normal")  # Включить кнопку после завершения


if __name__ == "__main__":
    app = BotConsoleWindow()
    app.mainloop()
