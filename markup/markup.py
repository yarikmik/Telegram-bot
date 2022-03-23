from telebot.types import KeyboardButton  # специальные типы бота для создания жлементов интерфейса
from settings import config  # импорт конфига
from data_base.dbalchemy import DBManager


class Keyboads:

    def __init__(self):
        self.markup = None
        self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам
        """
        return KeyboardButton(config.KEYBOARD[name])
