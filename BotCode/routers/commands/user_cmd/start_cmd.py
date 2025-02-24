# BotCode/routers/commands/user_cmd/start_cmd.py
# Работа с командой /start, для запуска бота

from BotLibrary import CommandHandler
from BotCode.keyboards import get_start_kb
user = "2"
# Создание команды /start
start_cmd = CommandHandler(
    name="start",
    description="Добро пожаловать!",
    keywords=["start", "старт", "запуск", "пуск", "on", "вкл", "с", "s", "ы",
              "ыефке", "cnfhn", "pfgecr", "gecr", "щт", "drk", "restart", "куыефке"],
    callbackdata="keywords",
    keyboard=get_start_kb,
    media="photo",
    path_to_media="ProjectsFiles/media/Banners/start_banner.jpg",
    tg_links=True,
    text_msg=f"""
Здравствуй, <b><a href="tg://user?id==<users>">дорогой Путник</a></b>. 
Мое имя - <i>Эми</i>! Я - ваш <i>путеводитель</i> в этом прекрасном месте!
Вы <b>готовы</b> отправиться в этот дивный мир?
""",
)
