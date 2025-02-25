# ProjectsFiles/configs/primoenv.py
# Загрузчик переменных из локального окружения

from os import getenv
from dotenv import load_dotenv

# Загружаем переменные из локального окружения
load_dotenv("ProjectsFiles/configs/.env")

# Токены от ботов телеграмма
bot_token = getenv("BOT_TOKEN")
bot1_token = getenv("BOT1_TOKEN")
bot2_token = getenv("BOT2_TOKEN")

# Ключи от API
api_key = getenv("API_KEY")
web_api_key = getenv("WEB_API_KEY")

# Хранилище сессии телеграмма
tg_api_uid = getenv("TG_API_UID")
tg_api_hash = getenv("TG_API_HASH")

# Айди администраторов проекта
admin_id = getenv("ADMIN_ID")
moderator_id = getenv("MODERATOR_ID")
tech_id = getenv("MYID")
bot_owner = getenv("OWNER")

# Айди пользователей, группы и канала
important_id = getenv("IMPORTANT_ID")
important_group_id = getenv("IMPORTANT_GROUP_ID")
important_channel_id = getenv("IMPORTANT_CHANNEL_ID")

# Айди тех.поддержки
secret = getenv("SECRET")