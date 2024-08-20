import json
from unittest.mock import mock_open, patch

from src.utils import make_the_python_objects_from_json


def test_make_the_python_objects_from_valid_json(to_json: tuple) -> None:
    """
    Тестирует создание объектов из корректного JSON-файла.

    :param to_json: Картеж данных для создания json-строк.
    :return: None.
    """
    json_data = json.dumps(to_json[0])  # [0] - валидные данные

    mocked_open = mock_open(read_data=json_data)
    with patch("builtins.open", mocked_open):
        with patch("os.path.exists", return_value=True):
            categories_utils, products_utils = make_the_python_objects_from_json("dummy_path.json")
            # Сравнение количества категорий
            assert len(categories_utils) == len(to_json[0])
            # Сравнение количества продуктов
            assert len(products_utils) == sum(len(category["products"]) for category in to_json[0])
            mocked_open.assert_called_once_with("dummy_path.json")


def test_make_the_python_objects_from_json_not_exist() -> None:
    """
    Тестирует работу функции с ненайденным файлом.

    :return: None.
    """
    with patch("os.path.exists", return_value=False) as mock_exists:
        categories_utils, products_utils = make_the_python_objects_from_json("dummy_path.json")
        assert categories_utils is None
        assert products_utils is None
        mock_exists.assert_called_once_with("dummy_path.json")


def test_make_the_python_objects_from_invalid_json() -> None:
    """
    Тестирует работу функции с JSON-файлом, который вызывает исключение при чтении.

    :return: None.
    """
    with patch("builtins.open", side_effect=IOError("Mocked IOError")) as mocked_open:
        with patch("os.path.exists", return_value=True):
            categories_utils, products_utils = make_the_python_objects_from_json("dummy_path.json")
            assert categories_utils is None
            assert products_utils is None
            mocked_open.assert_called_once_with("dummy_path.json")


def test_make_the_python_objects_from_json_invalid_category(to_json: tuple) -> None:
    """
    Тестирует работу функции с JSON-файлом, который содержит некорректные данные.

    :param to_json: Картеж данных для создания json-строк.
    :return: None.
    """
    json_data = json.dumps(to_json[1])  # [1] - отсутствует поле 'name' в словаре содержащем, информацию о категории

    mocked_open = mock_open(read_data=json_data)
    with patch("builtins.open", mocked_open):
        with patch("os.path.exists", return_value=True):
            categories_utils, products_utils = make_the_python_objects_from_json("dummy_path.json")
            assert categories_utils is None
            assert products_utils is None
            mocked_open.assert_called_once_with("dummy_path.json")


def test_make_the_python_objects_from_json_invalid_product(to_json: tuple) -> None:
    """
    Тестирует работу функции с JSON-файлом, который содержит некорректные данные.

    :param to_json: Картеж данных для создания json-строк.
    :return: None.
    """
    json_data = json.dumps(to_json[2])  # [2] - отсутствует поле 'name' в словаре, содержащем информацию о продукте

    mocked_open = mock_open(read_data=json_data)
    with patch("builtins.open", mocked_open):
        with patch("os.path.exists", return_value=True):
            categories_utils, products_utils = make_the_python_objects_from_json("dummy_path.json")
            assert categories_utils is None
            assert products_utils is None
            mocked_open.assert_called_once_with("dummy_path.json")
