# BotCode/utils/admin_lists.py
# Составления листа администраторов

from BotLibrary import bot

# Настройки экспорта в модули
__all__ = ("admin_lists",)


# Функция составления словаря администраторов
async def admin_lists(chat_id: int) -> str:
    admins = await bot.get_chat_administrators(chat_id)
    # Формируем список упоминаний администраторов
    admin_mentions = []
    for admin in admins:
        if admin.user.is_bot:
            continue
        admin_mentions.append(
            f"@{admin.user.username}" if admin.user.username else f"<a href=\"tg://user?id={admin.user.id}\">{admin.user.full_name}</a>")

    admins_text = ", ".join(admin_mentions) if admin_mentions else "Нет администраторов"
    return admins_text
