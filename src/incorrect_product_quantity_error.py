class IncorrectProductQuantityError(Exception):
    """Класс исключения при некорректном количестве товара."""

    def __init__(self, *args, **kwargs) -> None:
        """Конструктор для инициализации исключения с опциональным сообщением."""
        self.message = args[0] if args else "Невозможно добавить товар с нулевым количеством."

    def __str__(self) -> str:
        """Dunder-метод для строкового отображения исключения"""
        return self.message
