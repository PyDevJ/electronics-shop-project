import pytest
from src.phone import Phone


def test_init():
    phone1 = Phone("iPhone 14", 120_000, 5, 222)
    assert phone1.number_of_sim == 222


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.number_of_sim = 4
    assert phone1.number_of_sim == 4
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
