import json
import os

from src.category import Category
from src.product import Product


def make_the_python_objects_from_json(file_path: str = "data/products.json") -> tuple:
    """
    Возвращает картеж объектов полученный из JSON-файла.

    :param file_path: Путь до JSON-файла - опциональный параметр.
    :return:  Картеж объектов полученный из JSON-файла
    """
    # Проверка существования файла
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return None, None

    # Чтение JSON-файла
    try:
        with open(file_path) as file:
            data_list = json.load(file)

    except Exception as e:
        print(f"Ошибка чтения файла {file_path}: {e}.")
        return None, None

    # Пустые списки для сбора объектов
    categories_list = list()
    all_products_without_categories = list()

    # Получение данных для создания объектов
    for item in data_list:
        if not ("name" in item and "description" in item and "products" in item):
            print("В JSON-файле отсутствуют необходимые поля.")
            return None, None

        name_c = item["name"]
        description_c = item["description"]

        products_list = list()
        products = item["products"]

        for i in products:
            if not ("name" in i and "description" in i and "price" in i and "quantity" in i):
                print("В JSON-файле отсутствуют необходимые поля.")
                return None, None

            name_p = i["name"]
            description_p = i["description"]
            price_p = i["price"]
            quantity_p = i["quantity"]

            # Создание экземпляра класса Product
            product = Product(name_p, description_p, price_p, quantity_p)
            products_list.append(product)
            all_products_without_categories.append(product)

        # Создание экземпляра класса Category
        category = Category(name_c, description_c, products_list)
        categories_list.append(category)

    return categories_list, all_products_without_categories
