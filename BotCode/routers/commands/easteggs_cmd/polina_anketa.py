# BotCode/routers/commands/easteggs_cmd/polina_anketa.py
# Работа с командой /polina_za_tri_eleksira, для вывода анкеты

from BotLibrary import CommandHandler
from BotCode.keyboards import get_my_inline_kb

# Настройки экспорта в модули
__all__ = ("polina_za_tri_eleksira_cmd",)

# Шаблон анкеты
shablon_anketa = ("""📜 \\| **Статистика персонажа**  

👤 **Пользователь:** [Кейя](https://t.me/aiirries)  
🏅 **Ранг:** Участник 

📊 **Активность \(д\\|н\\|м\\|вс\):**  
🗨 **День:** 1\.0k \\| **Неделя:** 3\.6k \\| **Месяц:** 4\.1k \\| **Всего:** 894\.2M  

🏠 **Группа:** Сесбийки\-V 

🧭 **Состояние персонажа**  
❤️ **Здоровье:** ▰▰▰▰▱▱▱▱▱▱ \(40%\)  
🍖 **Голод:** ▰▰▰▰▰▰▰▰▰▱ \(90%\)  
🧠 **Рассудок:** ▰▰▰▰▰▰▰▰▰▱ \(90%\)  

📌 **Важные события**  
🕵 **Разведка:** Украла статую Сталина
🚩 **Победы:** Выжила при босс\-файте с Ефремовой
""")

# Создание команды /my с несколькими медиа
polina_za_tri_eleksira_cmd = CommandHandler(
    name="polina_za_tri_eleksira",
    description="Получение личной анкеты Поляка",
    keywords=["polina_za_tri_eleksira"],
    keyboard=get_my_inline_kb, callbackdata=["keywords"],
    media="photo", path_to_media=["ProjectsFiles/media/Anketa/polina_easteggs_anketa.jpeg"],
    text_msg=shablon_anketa,
    parse_mode="MarkdownV2",
)