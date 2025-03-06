# BotCode/keyboards/inline_kb/my_inline_kb.py
# Создание инлайн-клавиатуры на команду: /my

from BotLibrary import BaseInlineKeyboard

# Настройка экспорта в модули
__all__ = ("get_my_inline_kb",)

# Функция создания клавиатуры
def get_my_inline_kb(row_width : int = 2):
    buttons = [
        ("🔹Навыки", None, "skills_cbd"),
        ("🎒Инвентарь", None, "inventory_cbd"),
        ("👥Группа", None, "group_cbd"),
        ("💊Здоровье", None, "health_cbd"),
    ]
    return BaseInlineKeyboard(buttons, row_width=row_width).get_keyboard()
