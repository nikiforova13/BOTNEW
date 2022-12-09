from base_init import BaseInitTelebot
# импортируем основные настройки проекта
from settings import config


class TelBot(BaseInitTelebot):
    """
    Основной класс телеграмм бота (сервер), в основе которого
    используется библиотека pyTelegramBotAPI
    """
    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def start(self):
        """
        Метод предназначен для старта обработчика событий (старта проекта)
        """
        self.handler.start_handler()

    def run_bot(self):
        """
        Метод запускает основные события сервера
        """
        # обработчик событий
        self.start()
        # служит для запуска бота (работа в режиме нон-стоп)
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()
