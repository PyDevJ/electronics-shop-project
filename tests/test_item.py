"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount()
    assert item1.price == 8000.0


def test_name():
    item2 = Item("Смартфон", 10000, 20)
    item2.name = 'Смартфон'
    assert item2.name == 'Смартфон'
    item2.name = 'Наименование'
    assert item2.name == 'Наименован'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    no_item = 123
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Часы", 5000, 15)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Смартфон", 10000, 20, 3)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item2 + phone2 == 35
    assert type(phone1 + phone2) == int
    assert phone1 + no_item == 5
