from typing import List

from src.base_order_category_properties import BaseOrderCategoryProperties
from src.incorrect_product_quantity_error import IncorrectProductQuantityError
from src.product import Product


class Category(BaseOrderCategoryProperties):
    """Класс для представления категории."""

    # Атрибуты на уровне класса для ведения подсчетов
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """Dunder-метод для инициализации экземпляра класса Category."""
        super().__init__(name, description)
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Dunder-метод для строкового отображения информации об объекте."""
        total = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в экземпляр класса Category."""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise IncorrectProductQuantityError()
            except IncorrectProductQuantityError as e:
                print(e)
            else:
                self.__products.append(product)
                Category.product_count += 1
                print(f"Товар '{product.name}' успешно добавлен.")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError()

    def middle_price(self) -> float:
        """Метод для подсчета среднего ценника всех товаров."""
        total = sum(product.price for product in self.__products)
        try:
            avg = total / len(self.__products)
        except ZeroDivisionError:
            return 0.0
        else:
            return round(avg, 2)

    @property
    def products(self) -> str:
        """Геттер для получения списка продуктов в виде строк."""
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        """Геттер для получения списка продуктов."""
        return self.__products


class CategoryProductsIterator:
    """Вспомогательный класс для итерации по товарам в категории."""

    def __init__(self, category: Category) -> None:
        """Dunder-метод для инициализации итератора с объектом категории."""
        self.__category = category
        self.__index = 0

    def __iter__(self) -> "CategoryProductsIterator":
        """Dunder-метод для возврата итератора."""
        return self

    def __next__(self) -> Product:
        """Dunder-метод для получения следующего товара в категории."""
        if self.__index < len(self.__category.products_list):
            product = self.__category.products_list[self.__index]
            self.__index += 1
            return product
        else:
            raise StopIteration
