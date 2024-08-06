import pytest
from unittest.mock import patch
from io import StringIO

from src.main import Product, Category


def test_price_setter_with_valid_value():
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_with_invalid_value():
    product = Product("Test Product", "Test Description", 100.0, 10)

    with patch('sys.stdout', new=StringIO()) as fake_out:
        product.price = -50
        assert "Цена не должна быть нулевая или отрицательная" in fake_out.getvalue()

    with patch('sys.stdout', new=StringIO()) as fake_out:
        product.price = 0
        assert "Цена не должна быть нулевая или отрицательная" in fake_out.getvalue()


@patch('builtins.input', side_effect=['y'])
def test_price_decrease_confirmation(mock_input):
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = 50.0
    assert product.price == 50.0


@patch('builtins.input', side_effect=['n'])
def test_price_decrease_cancellation(mock_input):
    product = Product("Test Product", "Test Description", 100.0, 10)
    original_price = product.price
    product.price = 50.0
    assert product.price == original_price


def test_new_product_with_existing_product():
    existing_products = [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    ]
    new_product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 185000.0,
        "quantity": 3
    }
    updated_product = Product.new_product(new_product_data, existing_products)
    assert updated_product.quantity == 8  # 5 + 3
    assert updated_product.price == 185000.0


def test_new_product_with_no_existing_product():
    existing_products = [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    ]
    new_product_data = {
        "name": "Sony Xperia 1 III",
        "description": "256GB, Черный цвет",
        "price": 95000.0,
        "quantity": 10
    }
    new_product = Product.new_product(new_product_data, existing_products)
    assert new_product.name == "Sony Xperia 1 III"
    assert new_product.price == 95000.0
    assert new_product.quantity == 10


def test_get_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    products = category.products
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in products
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in products
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in products


if __name__ == "__main__":
    pytest.main()