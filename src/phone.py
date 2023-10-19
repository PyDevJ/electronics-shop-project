from src.item import Item


class Phone(Item):
    """
    `Phone` содержит все атрибуты класса `Item` и дополнительно атрибут,
    содержащий количество поддерживаемых сим-карт.
    """
    def __init__(self, name, price, quantity, number_sim):
        super().__init__(name, price, quantity)
        self.number_sim = number_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_sim})"

    @property
    def number_of_sim(self):
        return self.number_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        if new_number > 0:
            self.number_sim = new_number
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
