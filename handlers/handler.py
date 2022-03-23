import abc  # для абстрактны классов
from markup.markup import Keyboards  # разметка клавиатуры и клавиш
from data_base.dbalchemy import DBManager  # класс менеджер для работы с ДБ


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        self.bot = bot  # объект бота
        self.keybords = Keyboards()  # инициализация разметки кнопок
        self.BD = DBManager()  # инициализация менеждера работы с БД

    @abc.abstractmethod
    def handle(self):
        pass
