class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirmation = input(f"Цена понижается с {self.__price} до {value}. Вы уверены? (y/n): ")
            if confirmation.lower() == 'y':
                self.__price = value
                print(f"Цена обновлена на {self.__price}.")
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = value
            print(f"Цена обновлена на {self.__price}.")

    @classmethod
    def new_product(cls, product_data, existing_products):
        """
        Класс-метод для создания или обновления объекта Product из словаря.

        :param product_data: Словарь с параметрами товара, содержащий ключи 'name', 'description', 'price', 'quantity'.
        :param existing_products: Список существующих объектов Product для проверки дубликатов.
        :return: Обновленный или новый экземпляр класса Product.
        """
        product_name = product_data.get("name")
        product_description = product_data.get("description")
        product_price = product_data.get("price")
        product_quantity = product_data.get("quantity")

        # Поиск существующего товара
        for product in existing_products:
            if product.name == product_name:
                # Обновляем количество и цену
                product.quantity += product_quantity
                if product_price > product.price:
                    product.price = product_price
                print(f"Product '{product_name}' updated.")
                return product

        # Если товар не найден, создаем новый
        return cls(
            name=product_name,
            description=product_description,
            price=product_price,
            quantity=product_quantity
        )


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            self.add_product(product)
        Category.category_count += 1

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1
        print(f"Product '{product.name}' added to category '{self.name}'.")

    def update_product_quantity(self, product_name, quantity):
        for product in self.__products:
            if product.name == product_name:
                product.quantity = quantity
                print(f"Quantity of '{product_name}' updated to {quantity}.")
                return
        print(f"Product '{product_name}' not found in category '{self.name}'.")

    def get_products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print("\nСписок товаров в категории:")
    for product_info in category1.get_products():
        print(product_info)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print("\nОбновленный список товаров в категории:")
    for product_info in category1.get_products():
        print(product_info)

    print(f"\nОбщее количество товаров: {Category.product_count}")

    # Создание нового продукта или обновление существующего
    new_product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    new_product = Product.new_product(new_product_data, category1._Category__products)

    # Печать информации о новом или обновленном продукте
    print(
        f"\nНовый или обновленный продукт:\nНазвание: {new_product.name}\nОписание: {new_product.description}\nЦена: {new_product.price}\nКоличество: {new_product.quantity}")

    # Попробуем установить отрицательную цену
    new_product.price = -100
    print(f"\nОбновленная цена нового продукта: {new_product.price}")

    # Попробуем установить нулевую цену
    new_product.price = 0
    print(f"\nОбновленная цена нового продукта: {new_product.price}")

    # Попробуем установить цену ниже текущей
    new_product.price = 500
    print(f"\nОбновленная цена нового продукта: {new_product.price}")

    # Попробуем установить цену выше текущей
    new_product.price = 600
    print(f"\nОбновленная цена нового продукта: {new_product.price}")

