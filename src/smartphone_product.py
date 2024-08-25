from src.category import Product


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Конструктор для инициализации экземпляра класса Smartphone."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone") -> int:
        """Dunder-метод для сложения смартфонов и получения полной стоимости всех товаров на складе."""
        if type(other) is Smartphone:
            return round(self.price * self.quantity + other.price * other.quantity)
        raise TypeError()
