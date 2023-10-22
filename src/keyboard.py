from src.item import Item


class MixinLog:
    """
    Миксин для хранения и изменения раскладки клавиатуры.
    """
    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        """Изменяет язык раскладки клавиатуры с 'EN' на 'RU'."""
        if self.__language == "EN":
            self.__language = "RU"
            return self
        else:
            self.__language = "EN"
            return self

    @property
    def language(self):
        """Возвращает язык раскладки клавиатуры."""
        return self.__language


class Keyboard(Item, MixinLog):
    """
    Класс для товара “клавиатура”.
    """
