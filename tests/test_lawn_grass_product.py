import pytest

from src.lawn_grass_product import LawnGrass
from src.smartphone_product import Smartphone


def test_lawn_grass_init(lawn_grass1: LawnGrass) -> None:
    """
    Тестирует инициализацию экземпляра класса LawnGrass.

    :param lawn_grass1: Экземпляр класса LawnGrass.
    :return: None.
    """
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_lawn_grass_add(lawn_grass1: LawnGrass, lawn_grass2: LawnGrass) -> None:
    """
    Тестирует сложение продуктов класса LawnGrass.

    :param lawn_grass1: Экземпляр класса LawnGrass.
    :param lawn_grass2: Экземпляр класса LawnGrass.
    :return: None.
    """
    assert lawn_grass1 + lawn_grass2 == 16_750


def test_smartphone_add_smartphone(lawn_grass2: LawnGrass, smartphone2: Smartphone) -> None:
    """
    Тестирует сложение продуктов из разных категорий.

    :param lawn_grass2: Экземпляр класса LawnGrass.
    :param smartphone2: Экземпляр класса Smartphone.
    :return: None.
    """
    with pytest.raises(TypeError):
        lawn_grass2 + smartphone2


def test_smartphone_add_price(lawn_grass1: LawnGrass) -> None:
    """
    Тестирует сложение продуктов класса LawnGrass с ценой.

    :param lawn_grass1: Экземпляр класса LawnGrass.
    :return: None.
    """
    with pytest.raises(TypeError):
        lawn_grass1 + 1000
