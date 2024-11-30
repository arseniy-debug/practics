"1"
class Employee: #  Родительский класс Employee
    def __init__(self, base_salary):
        self.base_salary = base_salary


class Manager(Employee):
    def __init__(self, base_salary, management_bonus):
        super().__init__(base_salary)
        self.management_bonus = management_bonus # Бонус только для менеджеров

    def calculate_salary(self):
        return self.base_salary + self.management_bonus  # Добавляем бонус


class Developer(Employee):
    def __init__(self, base_salary, project_cost):
        super().__init__(base_salary)
        self.project_cost = project_cost # Плата за проект

    def calculate_salary(self):
        return self.base_salary + self.project_cost # Добавляем плату


BASE_SALARY = 50000

# зп зависит от бонуса у менеджера и от цены проекта у прогера
manager = Manager(BASE_SALARY, 10000)
developer = Developer(BASE_SALARY, 5000)

print(f"Зарплата менеджера: {manager.calculate_salary()} руб.")
print(f"Зарплата разработчика: {developer.calculate_salary()} руб.")


"2"
class Vehicle: #  Создаем родительский класс
    def __init__(self):
        self.doors = 0


class Car(Vehicle): # Создаем дочерние классы
    def __init__(self):
        super().__init__() # Берем информацию от родительского класса
        self.doors = 4

    def get_description(self):
        return f"машина - это транспортное средство с {self.doors} дверями."


class Bike(Vehicle): # Создаем дочерние классы
    def __init__(self):
        super().__init__() # Берем информацию от родительского класса

    def get_description(self):
        return f"велосипед - это транспортное средство без дверей, но с управляемым рулем"


class Trolleybus(Vehicle): # Создаем дочерние классы
    def __init__(self):
        super().__init__() # Берем информацию от родительского класса
        self.doors = 3

    def get_description(self):
        return f"троллейбус - это транспортное средство с {self.doors} дверьми."


car = Car()
bike = Bike()
trolleybus = Trolleybus()

print(f"Описание машины: {car.get_description()}")
print(f"Описание велосипеда: {bike.get_description()}")
print(f"Описание троллейбуса: {trolleybus.get_description()}")


"3"
from datetime import datetime
import time


class Product:
    def __init__(self, price, stock, category):
        self.price = price
        self.stock = stock
        self.category = category

    def buy(self, amount):  # Метод для покупки телефона
        self.stock -= amount


class Order:
    def __init__(self, amount, price):
        self.tax = 20
        self.discount = 10
        self.amount = amount
        self.price = price

    def calculate_with_tax(self, amount, price):  # Расчитываем цену с ндс
        return (amount * price) + ((amount * price) * (self.discount / 100))

    def calculate_discount(self, amount, price):  # Расчитываем скидку
        return self.calculate_with_tax(amount, price) * (order.discount / 100)


class Customer:
    def __init__(self, name, history):
        self.name = name
        self.history = []

    def add_history(self, history):  # Добавляем историю покупок
        self.history += history


class ShoppingCart:
    def __init__(self, amount):
        self.amount = amount

    def add_item(self, amount):  # Функция для добавления предмента
        self.amount += amount

    def delete_item(self, amount):  # Функция для удаления предмента
        self.amount -= amount


name = input("Введите ваше имя: ")

customer = Customer(name, [])
phone = Product(30000, 100, 'phone')
cart = ShoppingCart(0)
order = Order(0, 0)

while phone.stock > 0:
    amount = int(input(f"У нас в наличии есть {phone.stock} {phone.category} по цене {phone.price} за 1 единицу товара. Сколько бы вы хотели купить? "))
    if amount <= phone.stock:
        phone.buy(amount)
        cart.add_item(amount) # Добавляем в корзину
        print(f"У вас в корзине {cart.amount} предметов")

        answer = input("Хотели бы Вы изменть корзину? ").lower()
        if answer == "да":
            add_or_delete = input("Добавить или удалить товары из корзины? ").lower()
            if add_or_delete == "добавить":
                print(f"У вас в корзине {cart.amount} предметов")
                amount = int(input(f"У нас в наличии есть {phone.stock} {phone.category} по цене {phone.price} за 1 единицу товара. Сколько бы вы хотели купить? "))
                if amount <= phone.stock:
                    phone.buy(amount)
                    cart.add_item(amount) # Добавляем в корзину
                    print(f"У вас в корзине {cart.amount} предметов") # Обновление информации
                else:
                    print("У нас нет столько в наличии.")
            elif add_or_delete == "удалить":
                amount = int(
                    input(f"У вас в корзине {cart.amount} предметов, сколько предметов вы бы хотели удалить? "))
                if amount <= cart.amount:
                    phone.buy(amount)
                    cart.delete_item(amount) # Удаляем из корзину
                    print(f"У вас в корзине {cart.amount} предметов")  # Обновление информации
                else:
                    print("У вас нет столько в корзине.")
        elif answer == "нет":
            pass
        else:
            print("Такой опции нет.")

        print(f"Цена с учетом НДС: {order.calculate_with_tax(cart.amount, phone.price)} руб, ваша скидка составляет {order.discount}%, в рублях это {order.calculate_discount(cart.amount, phone.price)} руб.")
        print(f"Итоговая сумма покупки: {order.calculate_with_tax(cart.amount, phone.price) - order.calculate_discount(cart.amount, phone.price)}")

        print("Проводится оплата...")
        time.sleep(3) # Для реализма
        print("Оплата прошла успешно")

        cart.amount = 0

        customer.history += f"Время покупки: {str(datetime.now())[:19]}, количество товара: {cart.amount}, цена 1 ед. товара: {phone.price}"  # История
    else:
        print("У нас столько нет в наличии")


"4"
import random


class SpaceShip:
    def __init__(self):
        self.fuel = random.randint(50, 100)
        self.condition = random.randint(50, 100)
        self.velocity = 0
        self.distance_covered = 0

    def fly(self, amount):  # Метод полета
        self.fuel = max(0, self.fuel - amount)

    def repair(self, amount):  # Метод починки
        self.condition = min(100, self.condition + amount)

    def accelerate(self, speed):  # Метод ускорения
        if self.fuel > 0:
            self.velocity += speed
            self.distance_covered += speed // 4
            self.fly(speed // 4)

    def decelerate(self, speed):  # Метод замедления
        self.velocity = max(0, self.velocity - speed)


class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.health = random.randint(50, 100)
        self.skills = {  # Навыки
            "педалирование": random.randint(40, 100),
            "ремонт": random.randint(40, 100),
            "навигация": random.randint(40, 100),
        }

    def heal(self, amount):  # Хилимся
        self.health = min(100, self.health + amount)

    def repair_ship(self, spaceship):  # Чинимся
        repair_amount = random.randint(10, 30)
        spaceship.repair(repair_amount)


class Mission:
    def __init__(self, objectives):
        self.objectives = objectives
        self.resources = {"провизия": random.randint(50, 100), "кислород": random.randint(50, 100)}
        self.events = ["встреча с астероидом", "потеря топлива", "авария", "спокойный отрезок", "обнаружен ресурс"]

    def run(self, spaceship, crew):  # Метод для основного кода
        print("Миссия началась!")
        target_distance = random.randint(200, 300)  # Для реализма
        while spaceship.fuel > 0 and spaceship.condition > 0 and self.resources["кислород"] > 0:  # Проверка условий
            event = random.choice(self.events)
            print(f"Событие: {event}")
            if event == "встреча с астероидом":
                damage = random.randint(5, 15)
                spaceship.condition -= damage
                print(f"Корабль получил урон: -{damage} к состоянию корпуса.")
            elif event == "потеря топлива":
                fuel_loss = random.randint(5, 15)
                spaceship.fly(fuel_loss)
                print(f"Потеря топлива: -{fuel_loss}.")
            elif event == "авария":
                spaceship.condition -= random.randint(10, 20)
                for member in crew:
                    member.health -= random.randint(5, 15)
                print("Авария! Корабль и экипаж пострадали.")
            elif event == "спокойный отрезок":
                spaceship.accelerate(random.randint(15, 25))
                print("Спокойный участок пути, корабль ускорился.")
            elif event == "обнаружен ресурс":
                resource_gain = random.randint(15, 30)
                spaceship.fuel += resource_gain
                spaceship.repair(resource_gain)
                self.resources["кислород"] += random.randint(10, 20)
                print(f"Обнаружены ресурсы: +{resource_gain} к топливу, корпусу, и кислороду.")

            self.resources["кислород"] -= random.randint(3, 8)
            spaceship.distance_covered += spaceship.velocity // 10
            print(f"Корабль: топливо={spaceship.fuel}, корпус={spaceship.condition}, скорость={spaceship.velocity}, пройдено={spaceship.distance_covered}/{target_distance} км")
            print(f"Ресурсы: кислород={self.resources['кислород']}, провизия={self.resources['провизия']}")

            if spaceship.distance_covered >= target_distance:
                print("Миссия завершена успешно!")
                return

        if spaceship.fuel == 0:
            print("Миссия провалилась: закончилось топливо.")
        elif spaceship.condition <= 0:
            print("Миссия провалилась: корабль разрушен.")
        elif self.resources["кислород"] <= 0:
            print("Миссия провалилась: кончился кислород.")


ship = SpaceShip()
pilot = CrewMember(name="Мишка", role="Пилот")
salaga = CrewMember(name="Гришка", role="Салага")
mission = Mission(objectives=["Достичь орбиты Марса"])

mission.run(ship, [pilot, salaga])
