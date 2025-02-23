from tkinter import PhotoImage
import customtkinter as ctk  # модуль для создания стилизованных интерфейсов
from PIL import Image, ImageTk
from BotLibrary import *  # импорт настроек бота (например, имени, фамилии, и имени пользователя)

# Создание роутера и настройка экспорта
__all__ = ("App", )
command_text = "GUI"


# Настройка внешнего вида интерфейса
ctk.set_appearance_mode("System")  # Установка режима внешнего вида: "System", "Dark" или "Light"
ctk.set_default_color_theme("blue")  # Установка цветовой темы: "blue", "green", "dark-blue"


# Класс приложения, наследующий от customtkinter.CTk
class App(ctk.CTk):
    def __init__(self):
        super().__init__()  # Инициализация базового класса

        # Настройка главного окна
        self.title(f"{BotInfo.first_name} {BotInfo.last_name} - @{BotInfo.username}")  # Заголовок окна
        self.geometry(f"{700}x{580}")  # Размер окна (ширина x высота)

        # Настройка сетки (разметка окна на ячейки)
        self.grid_columnconfigure(0, weight=1)  # Установка растяжения для 1-го столбца (боковая панель)
        self.grid_columnconfigure(1, weight=9)  # Установка растяжения для 2-го столбца (содержимое вкладок)
        self.grid_rowconfigure((0, 1), weight=1)  # Установка растяжения для первых трех строк

        # Создание боковой панели
        self.sidebar_frame = ctk.CTkFrame(self, width=100, corner_radius=0)  # Рамка боковой панели с уменьшенной шириной
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")  # Расположение в сетке
        self.sidebar_frame.grid_rowconfigure(4, weight=1)  # Установка растяжения для 4-й строки

        # Логотип на боковой панели
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text=BotInfo.username,
                                       font=ctk.CTkFont(size=16, weight="bold"))  # Метка с текстом
        self.logo_label.grid(row=0, column=0, padx=10, pady=(20, 10))  # Расположение метки в сетке

        # Кнопки на боковой панели
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Консоль",
                                              command=self.switch_tab_console,
                                              font=ctk.CTkFont(size=14))
        self.sidebar_button_1.grid(row=1, column=0, padx=10, pady=10)  # Первая кнопка
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="База данных",
                                              command=self.switch_tab_database,
                                              font=ctk.CTkFont(size=14))
        self.sidebar_button_2.grid(row=2, column=0, padx=10, pady=10)  # Вторая кнопка
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, text="Иное",
                                              command=self.switch_tab_other,
                                              font=ctk.CTkFont(size=14))
        self.sidebar_button_3.grid(row=3, column=0, padx=10, pady=10)  # Третья кнопка

        # Новые кнопки "Запуск" и "Выключение"
        self.start_button = ctk.CTkButton(self.sidebar_frame, text="Запуск", command=self.start_button_click,
                                          font=ctk.CTkFont(size=14))
        self.start_button.grid(row=5, column=0, padx=10, pady=10)  # Кнопка "Запуск"

        self.stop_button = ctk.CTkButton(self.sidebar_frame, text="Выключение",
                                         command=self.stop_button_click,
                                         font=ctk.CTkFont(size=14))
        self.stop_button.grid(row=6, column=0, padx=10, pady=10)  # Кнопка "Выключение"

        # Элементы управления режимами и масштабированием интерфейса
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Тема UI", anchor="w",
                                                  font=ctk.CTkFont(size=12))
        self.appearance_mode_label.grid(row=7, column=0, padx=10, pady=(10, 0))  # Метка для выбора темы
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(
            self.sidebar_frame, values=["Светлая", "Темная", "Система"], command=self.change_appearance_mode_event
        )  # Меню выбора темы
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=10, pady=(10, 10))  # Расположение меню

        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="Масштабирование",
                                          anchor="w", font=ctk.CTkFont(size=12))  # Метка для масштабирования
        self.scaling_label.grid(row=9, column=0, padx=10, pady=(10, 0))  # Расположение метки
        self.scaling_optionemenu = ctk.CTkOptionMenu(
            self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event
        )  # Меню выбора масштаба
        self.scaling_optionemenu.grid(row=10, column=0, padx=10, pady=(10, 20))  # Расположение меню

        # Создание вкладок
        self.tabview = ctk.CTkTabview(self, width=250)  # Виджет вкладок
        self.tabview.grid(row=0, column=1, rowspan=3, columnspan=2, padx=(20, 0), pady=(20, 0),
                          sticky="nsew")  # Растягиваем на все пустое пространство
        self.tabview.add("Консоль")  # Первая вкладка
        self.tabview.add("База данных")  # Вторая вкладка
        self.tabview.add("Иное")  # Третья вкладка

        # Вкладка "Консоль" с текстовым полем
        self.textbox_tab_1 = ctk.CTkTextbox(self.tabview.tab("Консоль"))
        self.textbox_tab_1.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.textbox_tab_1.insert("0.0", "Текст в Textbox на вкладке Консоль\n\n")

        # Вкладка "База данных" с текстовым полем
        self.textbox_tab_2 = ctk.CTkTextbox(self.tabview.tab("База данных"))
        self.textbox_tab_2.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.textbox_tab_2.insert("0.0", "Текст в Textbox на вкладке База данных\n\n")

        # Вкладка "Иное" с текстовым полем
        self.textbox_tab_3 = ctk.CTkTextbox(self.tabview.tab("Иное"))
        self.textbox_tab_3.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.textbox_tab_3.insert("0.0", "Текст в Textbox на вкладке Иное\n\n")

        # Растягиваем строки и столбцы вкладок
        self.tabview.grid_rowconfigure(0, weight=1)  # Растягиваем строку, где находится текстовое поле
        self.tabview.grid_columnconfigure(0, weight=1)  # Растягиваем столбец, где находится текстовое поле

        # Убедитесь, что в каждой из вкладок разрешено растяжение:
        self.tabview.tab("Консоль").grid_rowconfigure(0, weight=1)
        self.tabview.tab("База данных").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Иное").grid_rowconfigure(0, weight=1)

        self.tabview.tab("Консоль").grid_columnconfigure(0, weight=1)
        self.tabview.tab("База данных").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Иное").grid_columnconfigure(0, weight=1)

        # Настройка элементов
        self.appearance_mode_optionemenu.set("Темная")  # Режим отображения установлен на "Dark"
        self.scaling_optionemenu.set("100%")  # Масштаб интерфейса установлен на 100%

        self.update()  # Принудительное обновление окна после создания

    def change_appearance_mode_event(self, new_appearance_mode: str):
        # Метод для изменения режима отображения интерфейса
        if new_appearance_mode == "Светлая":
            ctk.set_appearance_mode("Light")
        elif new_appearance_mode == "Темная":
            ctk.set_appearance_mode("Dark")
        elif new_appearance_mode == "Система":
            ctk.set_appearance_mode("System")

    def change_scaling_event(self, new_scaling: str):
        # Метод для изменения масштаба интерфейса
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        # Преобразование процента масштаба в дробное число
        ctk.set_widget_scaling(new_scaling_float)
        # Применение нового масштаба ко всем виджетам

    def switch_tab_console(self):
        # Переключение на вкладку "Консоль"
        self.tabview.grid(row=0, column=1, rowspan=3, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.set("Консоль")

    def switch_tab_database(self):
        # Переключение на вкладку "База данных"
        # Для возвращения вкладок
        self.tabview.grid(row=0, column=1, rowspan=3, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.set("База данных")

    def switch_tab_other(self):
        # Переключение на вкладку "Иное"
        self.tabview.grid(row=0, column=1, rowspan=3, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.set("Иное")

    def start_button_click(self):
        # Обработчик для кнопки "Запуск"
        print("Запуск")

    def stop_button_click(self):
        # Обработчик для кнопки "Выключение"
        print("Выключение")


# Начало кода и запуск GUI
if __name__ == "__main__":
    app = App()
    app.mainloop()
