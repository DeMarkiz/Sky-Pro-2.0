class PrintMixin:
    """
    Класс-миксин, который при создании объекта печатает в консоль информацию о том,
    как экземпляр класса был инициализирован.
    """

    def __init__(self) -> None:
        """Инициализация и вывод представления объекта."""
        print(repr(self))

    def __repr__(self) -> str:
        """Dunder-метод для возврата строкового представление объекта."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
