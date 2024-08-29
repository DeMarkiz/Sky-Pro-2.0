from src.base_order_category_properties import BaseOrderCategoryProperties
from src.incorrect_product_quantity_error import IncorrectProductQuantityError
from src.product import Product


class Order(BaseOrderCategoryProperties):
    """Класс для представления заказа."""

    def __init__(self, product: Product, quantity: int):
        """Конструктор для инициализации заказа."""
        try:
            if quantity == 0:
                raise IncorrectProductQuantityError()
            if quantity > product.quantity:
                raise IncorrectProductQuantityError(
                    f"Товар {product.name} в настоящее время на складе доступен в количестве "
                    f"{product.quantity} штук."
                )
        except IncorrectProductQuantityError as e:
            print(e)
        else:
            product.quantity -= quantity

            self.product = product
            super().__init__(product.name, product.description)
            self.quantity = quantity
            self.total_price = self.product.price * self.quantity

            print(f"Товар '{self.name}' успешно добавлен.")
        finally:
            print("Обработка добавления товара в заказ завершена.")

    def __str__(self) -> str:
        """Dunder-метод для строкового отображения информации о заказе."""
        return (
            f"Куплено: {self.name}, {self.quantity} шт.\n"
            f"Описание товара: {self.description}\n"
            f"Сумма покупки: {round(self.total_price)} руб"
        )
