import random
from datetime import datetime

# Приветствие
def greet(name):
    print(f"Привет, {name}! Сегодня {datetime.now().strftime('%d-%m-%Y %H:%M')}")

# Создаём меню случайных блюд
def generate_menu(n=5):
    dishes = ["Пицца", "Салат", "Суп", "Бургер", "Суши", "Паста", "Сэндвич"]
    menu = {}
    for i in range(n):
        dish = random.choice(dishes)
        price = random.randint(100, 500)
        menu[dish] = price
    return menu

# Печатаем меню
def print_menu(menu):
    print("Меню ресторана:")
    for dish, price in menu.items():
        print(f"{dish}: {price} руб")

# Случайный заказ
def random_order(menu):
    dish = random.choice(list(menu.keys()))
    qty = random.randint(1, 3)
    print(f"Заказ: {qty} x {dish} = {qty*menu[dish]} руб")
    return dish, qty

# Основной блок
if __name__ == "__main__":
    greet("Андрей")
    menu = generate_menu()
    print_menu(menu)
    for _ in range(3):
        random_order(menu)
