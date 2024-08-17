import pytest

from src.lawn_grass_product import LawnGrass
from src.smartphone_product import Smartphone


def test_smartphone_init(smartphone1: Smartphone) -> None:
    """
    Тестирует инициализацию экземпляра класса Smartphone.

    :param smartphone1: Экземпляр класса Smartphone.
    :return: None.
    """
    assert smartphone1.name == "Smartphone1"
    assert smartphone1.description == "Description1"
    assert smartphone1.price == 50_000
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == "Model X"
    assert smartphone1.memory == 250
    assert smartphone1.color == "Black"


def test_smartphone_add(smartphone1: Smartphone, smartphone2: Smartphone) -> None:
    """
    Тестирует сложение продуктов класса Smartphone.

    :param smartphone1: Экземпляр класса Smartphone.
    :param smartphone2: Экземпляр класса Smartphone.
    :return: None.
    """
    assert smartphone1 + smartphone2 == 650_000


def test_smartphone_add_lawn_grass(smartphone1: Smartphone, lawn_grass1: LawnGrass) -> None:
    """
    Тестирует сложение продуктов из разных категорий.

    :param smartphone1: Экземпляр класса Smartphone.
    :param lawn_grass1: Экземпляр класса LawnGrass.
    :return: None.
    """
    with pytest.raises(TypeError):
        smartphone1 + lawn_grass1


def test_smartphone_add_price(smartphone1: Smartphone) -> None:
    """
    Тестирует сложение продуктов класса Smartphone с ценой.

    :param smartphone1: Экземпляр класса Smartphone.
    :return: None.
    """
    with pytest.raises(TypeError):
        smartphone1 + 90_000
