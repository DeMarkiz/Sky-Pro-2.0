from src.product import Product


class LawnGrass(Product):
    """Класс для представления травы газонной."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Конструктор для инициализации экземпляра класса LawnGrass."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "LawnGrass") -> int:
        """Dunder-метод для сложения травы газонной и получения полной стоимости всех товаров на складе."""
        if type(other) is LawnGrass:
            return round(self.price * self.quantity + other.price * other.quantity)
        raise TypeError()
