# BotCode/routers/commands/easteggs_cmd/finaki_succub.py
# Работа с командой /finaki_succub, для вывода анкеты

from BotLibrary import CommandHandler
from BotCode.keyboards import get_my_inline_kb

# Настройки экспорта в модули
__all__ = ("finaki_succub_cmd",)

# Шаблон анкеты
shablon_anketa = ("""📜 \\| **Статистика персонажа**  

👤 **Пользователь:** [Е Лань: Цветок Орхидеи](https://t.me/fin_aki) 
🏅 **Ранг:** Участник 
🌀 **Раса:** Суккуб 

📊 **Активность \(д\\|н\\|м\\|всего\):**  
🗨 **День:** 69 \\| **Неделя:** 69 \\| **Месяц:** 69 \\| **Всего:** 69  

🏠 **Группа:** Мемори\-IX \\| Заместитель

🧭 **Состояние персонажа**  
❤️ **Здоровье:** ▰▰▰▰▰▰▰▱▱▱ \(70%\)  
🍖 **Голод:** ▰▰▰▰▰▰▰▰▱▱ \(80%\)  
🧠 **Рассудок:** ▰▰▰▰▰▰▱▱▱▱ \(60%\)  

📌 **Важные события**
🏠 **Бункер:** Создание нового бункера в северных окрестностях города
🕵 **Разведка:** Нашла временную базу культистов "Мертвой души"
🎒 **Поиски:** Обнаружила картину Художника "Чужой \- муза культистов"
""")


# Создание команды /my с несколькими медиа
finaki_succub_cmd = CommandHandler(
    name="finaki_succub",
    description="Получение личной анкеты Финаки",
    keywords=["finaki_succub"],
    keyboard=get_my_inline_kb,
    media="photo", path_to_media=["ProjectsFiles/media/Banners/finaki_my.jpeg"],
    text_msg=shablon_anketa,
    parse_mode="MarkdownV2",
)