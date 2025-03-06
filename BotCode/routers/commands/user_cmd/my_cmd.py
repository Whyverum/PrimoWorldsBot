# BotCode/routers/commands/user_cmd/my_cmd.py
# Работа с командой /my, для вывода анкеты

from BotLibrary import CommandHandler
from BotCode.keyboards import get_my_inline_kb

# Настройки экспорта в модули
__all__ = ("my_cmd",)

# Шаблон анкеты
shablon_anketa = """
📜 \\| **Статистика персонажа**  

👤 **Пользователь:** [Альбедо](http://t.me/verdise)  
🏅 **Ранг:** Администратор  

📊 **Активность \(д\\|н\\|м\\|вс\):**  
🗨 **День:** 1\.2k \\| **Неделя:** 34\.6k \\| **Месяц:** 234\.7k \\| **Всего:** 1\.2M  

🏠 **Группа:** Неополис\-I  

🧭 **Состояние персонажа**  
❤️ **Здоровье:** ▰▰▰▰▰▰▰▰▰▱ \(90%\)  
🍖 **Голод:** ▰▰▰▰▰▰▰▱▱▱ \(70%\)  
🧠 **Рассудок:** ▰▰▰▰▰▰▱▱▱▱ \(60%\)  

📌 **Важные события**  
🕵 **Разведка:** Обнаружена Лаборатория X\-18  
💀 **Смерть:** Удушение  

"""

# Создание команды /my с несколькими медиа
my_cmd = CommandHandler(
    name="my",
    description="Получение личной анкеты",
    keywords=["my", "ьн", "me", "ьу"],
    keyboard=get_my_inline_kb, callbackdata=["keywords"],
    media="photo", path_to_media=["ProjectsFiles/media/Anketa/albedo_anketa.png"],
    text_msg=shablon_anketa,
    parse_mode="MarkdownV2",
)
