import pytest

from src.category import Category, CategoryProductsIterator


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


def test_category_add_product(categories: tuple, products: tuple) -> None:
    """
    Тестирует метод add_product.

    :param categories: Картеж экземпляров класса Category.
    :param products: Картеж экземпляров класса Product.
    :return: None.
    """
    categories[0].add_product(products[2])
    assert Category.product_count == 4


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
