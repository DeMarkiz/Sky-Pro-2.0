import pytest

from src.order import Order
from src.smartphone_product import Smartphone


def test_order_init(smartphone1: Smartphone) -> None:
    """
    Тестирует покупку товара без ошибки.

    :param smartphone1: Экземпляр класса Smartphone.
    :return: None.
    """
    quantity = smartphone1.quantity
    order1 = Order(smartphone1, 3)

    # Тест количества товара на складе после покупки
    assert quantity - 3 == smartphone1.quantity

    assert order1.product.price == smartphone1.price
    assert order1.name == smartphone1.name
    assert order1.description == smartphone1.description
    assert order1.quantity == 3
    assert order1.total_price == 150_000


def test_order_init_not_enough_error(capsys, smartphone1: Smartphone) -> None:
    """
    Тестирует покупку товара с нехваткой нужного количества товара на складе.

    :param capsys: Фикстура для перехвата вывода.
    :param smartphone1: Экземпляр класса Smartphone.
    :return: None.
    """
    Order(smartphone1, 6)
    message = capsys.readouterr()
    assert message.out.split("\n")[1] == "Товар Smartphone1 в настоящее время на складе доступен в количестве 5 штук."


def test_order_init_zero_error(capsys, smartphone1: Smartphone) -> None:
    """
    Тестирует заказ товара с нулевым количеством.

    :param capsys: Фикстура для перехвата вывода.
    :param smartphone1: Экземпляр класса Smartphone.
    :return: None.
    """
    # try
    Order(smartphone1, 0)

    message = capsys.readouterr()
    failed, completed = message.out.strip().split("\n")[1:]

    # except
    assert failed == "Невозможно добавить товар с нулевым количеством."

    # finally
    assert completed == "Обработка добавления товара в заказ завершена."




def test_order_str(smartphone1: Smartphone) -> None:
    """
    Тестирует строковое отображения информации о заказе.

    :param smartphone1: Экземпляр класса Smartphone.
    :return: None.
    """

    order1 = Order(smartphone1, 2)

    info_string = str(order1)
    expected = "Куплено: Smartphone1, 2 шт.\n" "Описание товара: Description1\n" "Сумма покупки: 100000 руб"

    assert info_string == expected
