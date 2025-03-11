# BotCode/routers/commands/user_cmd/start_time_cmd.py
#

from BotLibrary import CommandHandler
from BotCode.utils import get_weather

__all__ = ("weather_cmd",)

weather_cmd = CommandHandler(
    name="weather",
    description="Погода",
    keywords=["weather", "gjujlf", "цуферук", "погода"],
    media="command",
    func=[get_weather],
)
