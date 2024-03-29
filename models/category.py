# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, String, Integer, Boolean
# класс-конструктор для работы с декларативным стилем работы с SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# инициализация декларативного стиля
Base = declarative_base()


class Category(Base):
    """
    Класс для описания таблицы "Категория товара"
    """
    __tablename__ = 'category'  # Имя таблицы


    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    is_active = Column(Boolean)

    def __str__(self):
        return self.name
