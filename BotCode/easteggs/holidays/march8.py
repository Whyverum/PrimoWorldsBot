# BotCode/easteggs/holidays/8March.py
# Работа с командой /march8, для вывода поздравления с 8 Марта!

from BotLibrary import CommandHandler
from BotCode.keyboards import get_march8_inline_kb, get_return_march8_inline_kb

# Настройки экспорта в модули
__all__ = ("March8", "March8_Finaki", "March8_finik", "March8_kataz", "March8_sleshik", "March8_polina")

march8_happy_text = ("""🌸 <b>С 8 Марта!</b> 🌸
Вы наши дорогие девушки, мы хотим поздравить вас в честь этого праздника!
Пусть этот день принесёт вам <i>море улыбок</i>, <i>приятные воспоминания</i> и <i>теплые слова</i>! 🌷
Пусть каждый день будет наполнен <b>радостью</b>, <b>счастьем</b> и <b>любовью</b>, а мечты сбываются <b>легко и красиво!</b> 💐

Оставайтесь такими же прекрасными, вдохновляющими и неповторимыми! ✨ С праздником! 💖
Вы и сами знаете, что нужно сделать. Тогда <i>Вперед за Истиной</i>, наши любимые!""")
finaki_text = ("""
Финаки, милая, поздравляем тебя с 8 Марта!🌸 Помни и старайся не забывать, о том, что все таки по настоящему важно.
Ты сильно повзрослела, за то время сколько мы знакомы и я рад видеть, как ты превращаешься из той мелкой балбески-финаки, во взрослую Аню.💪
Надеюсь, что ты все также будешь покорять вершины, а главное не будешь ничего бояться. С 8 Марта Финаки!✨
""")
lostic_text = ("""
Слешик-Лостик, сколько имен, но ты навсегда останешься для нас той самой малышкой, с которой мы прошли через огонь, воду и медные кафешки. 🌸
Желаем тебе только счастья, чтобы с каждым днем ты становилась всё более радостной и яркой. Пусть твои глаза никогда не наполняются слезами, а сердце всегда согревает любовь и счастье. ❤️
Слешик, с 8 Марта! Радуйся и дари радость всем вокруг, милаш! ✨ Ты заслуживаешь только самого лучшего, пусть каждый твой день будет наполнен теплом и светом!
""")
kataz_text = ("""
Катаз? А это кто? 😜
Хахах, мы шутим! Катаз, с 8 Марта! 🌸 Помним тебя такой мелкой, а теперь уже, смотри, мешки с песком совращаешь! 💪 Расти, развивайся, не забывай учиться и, главное, думай, ведь ты всегда была умницей, Катазик! 🤔
Пусть этот день принесет тебе море радости, а впереди будет только светлое будущее. Помни, что именно поэтому ты — Катазик! 🌟
С праздником, кактус! 🌵 С праздником! Пусть каждый день будет полон ярких моментов и вдохновения! 🎉
""")
finik_text = ("""
def main(): print("Ох, кажется, что-то не тому мы это пишем! Финик, малыш, с 8 Марта! 🌸 Многое изменилось, как и ты, но даже так, я безмерно рад, что знаком с таким удивительным нефоренком!🌟)
Расти, познавай мир и следуй за Истиной! То, что мы найдем с тобой - это место, место, в кототором мы впервые услышим твой смех, а не крики от ужастиков😂 Будь умницей,")
мы ведь тобой очень дорожим.❤️ С праздником, малыш!✨
""")
polina_text = ("""
Полина-Полина, с тобой мы знакомы меньше всего, но уже ты стала нам очень дорогим человеком и настоящей подругой. 🌸 Ты как цветок, что появился из пепла — как же он звался? Не важно… Главное, что ты, как этот цветок, продолжаешь расцветать, быть такой же уникальной и прекрасной, как нечто совершенно особенное, созданное из другой материи. 💫
С 8 Марта, балбеска! 😄 Пусть этот день будет полон радости и вдохновения! Мы всегда будем рады выслушать твои истории и, главное, поддержать тебя в любом начинании. Ты заслуживаешь только самого лучшего!
Будь умничкой, Поляк! 🌷
""")



# Создание команды /march8 с несколькими медиа
March8 = CommandHandler(
    name="march8",
    description="Поздравление с 8 Марта!",
    keywords=["march8"],
    keyboard=get_march8_inline_kb, delete_msg=True,
    media="photo", path_to_media=["ProjectsFiles/media/Banners/march8_banner.jpeg"],
    text_msg=march8_happy_text,
)


# Создание команды /march8_finaki
March8_Finaki = CommandHandler(
    name="march8_finaki",
    description="Поздравление с 8 Марта Финаки!",
    keywords=["march8_finaki"],
    keyboard=get_return_march8_inline_kb, delete_msg=True,
    media="photo", path_to_media=["ProjectsFiles/media/Banners/march8_finaki_banner.jpeg"],
    text_msg=finaki_text,
)


# Создание команды /march8_finik
March8_finik = CommandHandler(
    name="march8_finik",
    description="Поздравление с 8 Марта Финик!",
    keywords=["march8_finik"],
    keyboard=get_return_march8_inline_kb, delete_msg=True,
    media="photo", path_to_media=["ProjectsFiles/media/Banners/march8_finik_banner.jpeg"],
    text_msg=finik_text,
)

# Создание команды /march8_polina
March8_polina = CommandHandler(
    name="march8_polina",
    description="Поздравление с 8 Марта Полина!",
    keywords=["march8_polina"],
    keyboard=get_return_march8_inline_kb, delete_msg=True,
    media="photo", path_to_media=["ProjectsFiles/media/Banners/march8_polina_banner.png"],
    text_msg=polina_text,
)

# Создание команды /march8_kataz
March8_kataz = CommandHandler(
    name="march8_kataz",
    description="Поздравление с 8 Марта Катаз!",
    keywords=["march8_kataz"],
    keyboard=get_return_march8_inline_kb, delete_msg=True,
    media="photo", path_to_media=["ProjectsFiles/media/Banners/march8_kataz_banner.png"],
    text_msg=kataz_text,
)

# Создание команды /march8_sleshik
March8_sleshik = CommandHandler(
    name="march8_sleshik",
    description="Поздравление с 8 Марта Слешик!",
    keywords=["march8_sleshik"],
    keyboard=get_return_march8_inline_kb, delete_msg=True,
    media="photo", path_to_media=["ProjectsFiles/media/Banners/march8_lostik_banner.png"],
    text_msg=lostic_text,
)