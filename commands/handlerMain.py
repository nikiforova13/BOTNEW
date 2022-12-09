from commands.handler_commands import CommandsBot
from base_init import BaseInitTelebot

class HandlerMain():
    """
    Главный обработчик событий
    """

    def start_handler(self):
        CommandsBot.handles()
