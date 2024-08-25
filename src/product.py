from typing import List

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для представления продукта."""

    # Атрибут на уровне класса для хранения экземпляров класса в виде списка
    all_products: List["Product"] = list()

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Dunder-метод для инициализации экземпляра класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

        Product.all_products.append(self)

    def __str__(self) -> str:
        """Dunder-метод для строкового отображения информации об объекте."""
        return f"{self.name}, {round(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> int:
        """Dunder-метод для сложения товаров и получения полной стоимости всех товаров на складе."""
        if isinstance(other, Product):
            return round(self.price * self.quantity + other.price * other.quantity)
        raise TypeError()

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        """Класс-метод для создания нового продукта или обновления существующего."""
        name = product_dict.get("name", "")
        description = product_dict.get("description", "")
        price = product_dict.get("price", 0.0)
        quantity = product_dict.get("quantity", 0)

        # Проверка наличия такого же товара схожего по имени
        for product in Product.all_products:
            if name == product.name:
                # Обновление количества товара
                product.quantity += quantity
                # Обновление цены, если новая цена выше
                if price > product.price:
                    product.price = price
                return product

        # Создание нового товара, если не найдено совпадений
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, amount: float) -> None:
        """Сеттер для установки цены."""
        if amount <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif amount < self.__price:
            difference = self.__price - amount
            confirmation = input(f"Вы уверены, что хотите снизить цену на {difference} руб? (y/n): ").lower()
            if confirmation == "y":
                self.__price = amount
            else:
                print("Цена осталась прежней")
        else:
            self.__price = amount
