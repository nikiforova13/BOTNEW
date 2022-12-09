# импортируем специальные типы телеграм бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
# импортируем настройки и утилиты
from settings import config


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """

    # инициализация разметки
    def __init__(self, markup):
        self.markup = None

    def set_btn_menu(self):
        """
        Создает кнопку
        """
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton("help")
        btn2 = KeyboardButton("search")
        btn3 = KeyboardButton("test")
        btn4 = KeyboardButton("professions")
        return markup.add(btn1, btn2, btn3, btn4)
