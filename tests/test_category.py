import pytest

from src.category import Category, CategoryProductsIterator
from src.product import Product


def test_category_init(categories: tuple, category_info: tuple, products: tuple) -> None:
    """
    Тестирует корректность инициализации объектов класса Category.

    :param categories: Картеж экземпляров класса Category.
    :param category_info: Картеж атрибутов экземпляра класса Category.
    :param products: Картеж экземпляров класса Product.
    :return: None.
    """
    products_str = "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.\n" "Iphone 15, 210000 руб. Остаток: 8 шт."

    assert categories[0].name == category_info[0]
    assert categories[0].description == category_info[1]
    assert categories[0].products == products_str  # Тест products-геттера


def test_category_category_count(category_count: int) -> None:
    """
    Тестирует подсчет количества продуктов.

    :param category_count: Результат вызова метода category_count.
    :return: None.
    """
    assert category_count == 2


def test_category_product_count(product_count: int) -> None:
    """
    Тестирует подсчет количества категорий.

    :param product_count: Результат вызова метода product_count.
    :return: None.
    """
    assert product_count == 3


def test_category_add_product(capsys, categories: tuple, products: tuple) -> None:
    """
    Тестирует метод add_product.

    :param capsys: Фикстура для перехвата вывода.
    :param categories: Картеж экземпляров класса Category.
    :param products: Картеж экземпляров класса Product.
    :return: None.
    """
    # try
    categories[0].add_product(products[2])

    message = capsys.readouterr()
    successfully, completed = message.out.strip().split("\n")

    # else
    assert Category.product_count == 4
    assert successfully == "Товар '55\" QLED 4K' успешно добавлен."

    # finally
    assert completed == "Обработка добавления товара завершена."


def test_category_add_product_zero_error(capsys, categories: tuple) -> None:
    """
    Тестирует метод add_product с нулевым количеством товара.

    :param capsys: Фикстура для перехвата вывода.
    :param categories: Картеж экземпляров класса Category.
    :return: None.
    """
    product = Product("Тест", "Количество: 0", 10, 1)
    product.quantity = 0  # количество товара: 0
    # try
    categories[0].add_product(product)

    message = capsys.readouterr()
    failed, completed = message.out.strip().split("\n")[1:]

    assert Category.product_count == 4

    # except
    assert failed == "Невозможно добавить товар с нулевым количеством."

    # finally
    assert completed == "Обработка добавления товара завершена."


def test_category_add_product_error(categories: tuple, products: tuple) -> None:
    """
    Тестирует метод add_product при вызове исключения TypeError.

    :param categories: Картеж экземпляров класса Category.
    :param products: Картеж экземпляров класса Product.
    :return: None.
    """
    with pytest.raises(TypeError):
        categories[0].add_product("product")


def test_category_str(categories: tuple) -> None:
    """
    Тестирует отображение информации о категории в виде строки.

    :param categories: Картеж экземпляров класса Category.
    :return: None.
    """
    category = categories[0]
    assert str(category) == "Смартфоны, количество продуктов: 20 шт."


def test_category_products_iterator(categories: tuple) -> None:
    """
    Тестирует итератор продуктов категории.

    :param categories: Картеж экземпляров класса Category.
    :return: None.
    """
    category = categories[0]
    expected = ["Samsung Galaxy S23 Ultra", "Iphone 15", '55" QLED 4K']

    assert [product.name for product in CategoryProductsIterator(category)] == expected


def test_middle_price(categories) -> None:
    """
    Тестирует подсчет среднего ценника всех товаров.

    :param categories: Картеж экземпляров класса Category.
    :return: None.
    """
    assert categories[0].middle_price() == 171_000.0


def test_middle_price_empty() -> None:
    """
    Тестирует подсчет среднего ценника в пустом списке товаров.

    :return: None.
    """
    category = Category("Category", "Description", [])
    assert category.middle_price() == 0.0
