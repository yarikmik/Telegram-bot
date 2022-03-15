# компоненты библиотеки для описания структуры таблицы
from sqlalchemy import Column, DateTime, Integer, ForeignKey
# импортируем модуль для связки таблиц
from sqlalchemy.orm import relationship, backref
# класс-конструктор для работы с декларативным стилем работы с SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# импортируем модель продуктов для связки моделей
from models.product import Products


# инициализация декларативного стиля
Base = declarative_base()

class Order(Base):
    """
    Таблица "Заказ"
    """

    __tablename__ = 'orders'  # Имя таблицы

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('product.id'))
    user_id = Column(Integer)

    products = relationship(
        Products,
        backref=backref('orders',
                        uselist=True,
                        cascade='delete,all'))

    def __str__(self):
        return f"{self.quantity} {self.data}"