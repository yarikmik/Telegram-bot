# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
# импортируем модуль для связки таблиц
from sqlalchemy.orm import relationship, backref
# класс-конструктор для работы с декларативным стилем работы с SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# импортируем модель Категория для связки моделей
from models.category import Category

# инициализация декларативного стиля
Base = declarative_base()

class Sales(Base):
    """
    Таблиуа "Акции"
    """

    __tablename__ = 'sales'  # Имя таблицы
