from src.lawn_grass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


def test_print_mixin(capsys) -> None:
    """
    Тест печати строкового представления объекта при инициализации.

    :param capsys: Фикстура для перехвата вывода.
    :return: None.
    """

    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone("Smartphone1", "Description1", 50_000.0, 5, 98.2, "Model X", 250, "Black")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Smartphone1, Description1, 50000.0, 5)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
