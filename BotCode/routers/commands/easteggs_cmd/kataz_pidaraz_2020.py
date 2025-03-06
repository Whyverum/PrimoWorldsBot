# BotCode/routers/commands/easteggs_cmd/kataz_pidaraz_2020.py
# Работа с командой /kataz_pidaraz_2020, для вывода анкеты

from BotLibrary import CommandHandler
from BotCode.keyboards import get_my_inline_kb

# Настройки экспорта в модули
__all__ = ("kataz_pidaraz_2020_cmd",)

# Шаблон анкеты
shablon_anketa = ("""📜 \\| **Статистика персонажа**  

👤 **Пользователь:** [Кунникудзуши](https://t.me/Kataaaz)  
🏅 **Ранг:** Участник 

📊 **Активность \(д\\|н\\|м\\|вс\):**  
🗨 **День:** 2 \\| **Неделя:** 3 \\| **Месяц:** 69 \\| **Всего:** 78  

🏠 **Группа:** Сесбийки\-V \\| Лидер

🧭 **Состояние персонажа**  
❤️ **Здоровье:** ▰▱▱▱▱▱▱▱▱▱ \(10%\)  
🍖 **Голод:** ▰▰▰▰▰▰▰▰▰▰ \(100%\)  
🧠 **Рассудок:** ▰▰▰▱▱▱▱▱▱▱ \(30%\)  

📌 **Важные события**  
🕵 **Разведка:** Обнаружила псих\.больницу\. \. Такую знакомую?  
🎒 **Поиски:** Нашла свою совесть  
""")


# Создание команды /my с несколькими медиа
kataz_pidaraz_2020_cmd = CommandHandler(
    name="kataz_pidaraz_2020",
    description="Получение личной анкеты Катаза",
    keywords=["kataz_pidaraz_2020"],
    keyboard=get_my_inline_kb, callbackdata=["keywords"],
    media="photo", path_to_media=["ProjectsFiles/media/Anketa/kataz_easteggs.jpeg"],
    text_msg=shablon_anketa,
    parse_mode="MarkdownV2",
)