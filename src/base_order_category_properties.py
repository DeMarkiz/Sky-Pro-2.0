from abc import ABC, abstractmethod


class BaseOrderCategoryProperties(ABC):
    """Абстрактный базовый класс для общих свойств классов Заказ и Категория."""

    def __init__(self, name: str, description: str) -> None:
        """Инициализация общих свойств."""
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового отображения информации об объекте."""
        pass
