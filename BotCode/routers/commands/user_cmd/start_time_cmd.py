# BotCode/routers/commands/user_cmd/start_time_cmd.py
# Работа с командой /start_time, для получения времени запуска бота

from BotLibrary import CommandHandler, BotInfo
from BotLibrary import dp

__all__ = ("start_time_cmd",)

start_time_cmd = CommandHandler(
    name="start_time",
    description="Время запуска бота",
    keywords=["start_time", "stime", "старт_время", "время_старта", "с_время",
              "ыефке_ешьу", "ыешьу", "cnfhn_dhtvcz", "dhtvz_cnfhnf", "c_dhtvz",
              "бот_время", "время_запуска", "бот_врем", "on_time", "щт_ешьу"],
    text_msg=lambda: f"Бот @{BotInfo.username} запущен: "
                     f"\nХост: <b>{dp['started_at']}</b> "
                     f"\nМСК: <b>{dp['started_at_msk']}</b>",
)
