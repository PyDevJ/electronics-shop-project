import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name  # атрибут `name` сделать приватным
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """Магический метод `__repr__`."""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Магический метод `__str__`."""
        return f"{self.name}"

    # добавить геттер для `name`, используя @property
    @property
    def name(self):
        return self.__name

    # добавить сеттер для `name`
    @name.setter
    def name(self, len_name):  # проверяет, что длина наименования товара не больше 10 символов
        if len(len_name) > 10:
            self.__name = len_name[:10]
        else:
            self.__name = len_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        """Инициализирует экземпляры класса из 'csv' файла."""
        path = os.path.relpath('../' + path, '')
        cls.all.clear()
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(name=row.get('name'), price=row.get('price'), quantity=row.get('quantity'))

    @staticmethod
    def string_to_number(number):
        """Статический метод, возвращающий число из числа-строк."""
        r_number = number.replace('.', '', 1).isdigit()
        if r_number:
            o_number = float(number)
            return int(o_number)

    def __add__(self, other):
        """
        Реализует проверку, чтобы нельзя было сложить `Phone` или `Item`
        с экземплярами не `Phone` или `Item` классов.
        """
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return self.quantity
