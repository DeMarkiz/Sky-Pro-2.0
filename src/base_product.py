from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для представления продукта."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> "BaseProduct":
        """Абстрактный класс-метод для создания нового продукта или обновления существующего."""
        pass
