from base_init import BaseInitTelebot
from Constants import const
from Markup import markup


class CommandsBot(BaseInitTelebot):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на кнопоки
    """

    def handles(self):
        """
        Обработка события нажатия на кнопку '/start'. Начало работы бота
        """

        @self.bot.message_handler(commands=["start"])
        def start(message):
            if message == '/start':
                mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}, {const.MESSAGE_START}</u></b>.'
                self.bot.send_message(message.from_user.id, text=mess, parse_mode='html',
                                      reply_markup=markup.Keyboards.set_btn_menu())
