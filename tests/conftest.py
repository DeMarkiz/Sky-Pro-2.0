import pytest

from src.category import Category
from src.lawn_grass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2],
)
category2 = Category(
    "Телевизоры",
    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    [product3],
)


@pytest.fixture
def products() -> tuple:
    """
    Фикстура, использующаяся для тестирования классов Product и Category.

    :return: Картеж экземпляров класса Product.
    """
    return product1, product2, product3


@pytest.fixture
def categories() -> tuple:
    """
    Фикстура, использующаяся для тестирования класса Category.

    :return: Картеж экземпляров класса Category.
    """
    return category1, category2


@pytest.fixture
def category_info() -> tuple:
    """
    Фикстура, использующаяся для тестирования класса Category.

    :return: Картеж атрибутов экземпляра класса Category.
    """
    return (
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )


@pytest.fixture
def category_count() -> int:
    """
    Фикстура, возвращающая результат вызова метода category_count.

    :return: Результат вызова метода category_count.
    """
    return Category.category_count


@pytest.fixture
def product_count() -> int:
    """
    Фикстура, возвращающая результат вызова метода product_count.

    :return: Результат вызова метода product_count.
    """
    return Category.product_count


@pytest.fixture
def to_json() -> tuple:
    """
    Фикстура для тестирования функции make_the_python_objects_from_json.

    :return: Картеж данных для тестирования функции.
    """
    return (
        [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не только коммуникации,\
                но и получение дополнительных функций для удобства жизни",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                    {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
                ],
            },
            {
                "name": "Телевизоры",
                "description": "Современный телевизор, который позволяет наслаждаться просмотром,\
                станет вашим другом и помощником",
                "products": [
                    {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
                ],
            },
        ],
        [{"description": "test"}],
        [{"name": "test", "description": "test", "products": [{"description": "test"}]}],
    )


@pytest.fixture
def product_dict() -> tuple:
    """
    Фикстура для тестирования создания продукта из словаря.

    :return: Данные в виде картежа словарей для создания продуктов.
    """
    return (
        {"name": "Phone", "description": "Some description", "price": 10000, "quantity": 1},
        {"name": "Phone", "description": "Some description", "price": 20000, "quantity": 1},
        {"name": "Phone", "description": "Some description", "price": 5000, "quantity": 1},
    )


@pytest.fixture
def smartphone1() -> Smartphone:
    """
    Фикстура для тестирования класса Smartphone.

    :return: Экземпляр класса Smartphone.
    """
    return Smartphone("Smartphone1", "Description1", 50_000.0, 5, 98.2, "Model X", 250, "Black")


@pytest.fixture
def smartphone2() -> Smartphone:
    """
    Фикстура для тестирования класса Smartphone.

    :return: Экземпляр класса Smartphone.
    """
    return Smartphone("Smartphone2", "Description2", 40_000.0, 10, 78.2, "Model Y", 150, "White")


@pytest.fixture
def lawn_grass1() -> LawnGrass:
    """
    Фикстура для тестирования класса LawnGrass.

    :return: Экземпляр класса LawnGrass.
    """
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass2() -> LawnGrass:
    """
    Фикстура для тестирования класса LawnGrass.

    :return: Экземпляр класса LawnGrass.
    """
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
