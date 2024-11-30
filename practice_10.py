"1"
class Rectangle:
    def __init__(self, width, height):
      self.width = width
      self.height = height

    def calculate_area(self):
      return f"Площадь прямоугольника: {self.width*self.height}"

    def calculate_perimeter(self):
      return f"Периметр прямоугольника: {2 * (self.width+self.height)}"

    def show_dementions(self):
      return f"Ширина прямоугольника: {self.width}, Высота прямоугольника: {self.height}"


rect = Rectangle(5, 4)
print(rect.calculate_area())
print(rect.calculate_perimeter())
print(rect.show_dementions())


"2"
class BankAccountсо:
    def __init__(self, account_holder):
      self.account_holder = account_holder
      self.balance = 0

    def deposit(self, amount):
      self.balance += amount

    def withdraw(self, amount):
      self.balance -= amount

    def get_balance(self):
      return f"Баланс счета: {self.balance}"

bank = BankAccountсо("Джо Байден")
bank.deposit(1200)
bank.withdraw(500)
print(bank.get_balance())


"3"
from random import randint


class Knight:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.gold = 1000

  def withdraw(self, gold):
    self.gold -= gold


class Dragon:
  def __init__(self, hp, damage):
    self.name = "Ящерица"
    self.hp = hp
    self.damage = damage


print("Где-то в 15 веке жил рыцарь, и завли его ...")  # мини-сюжет
name = str(input("Введите имя вашего рыцаря: "))
knight = Knight(name, 100, 100)
dragon = Dragon(300, 100)
print("И однажды дракон украл у рыцаря " + knight.name + " принцессу, и для того, чтобы получить ее назад, рыцарь " + knight.name + "должен победить дракона")
print("Для того, чтобы сражаться, нужно хорошенько подготовиться к бою, и для этого рыцарь " + knight.name + " отправился в таверну для покупки необходимого обмундирования и оружия")
print("У вас есть 1000 золота, на которые вы можете потратить на оружие и доспехи")

while knight.gold >= 200:  # цикл для покупки вещей
    buy = input("Что бы вы хотели купить?\n| Оружие |\n| Доспехи |\n").lower().strip()
    if buy == "оружие":
        weapon = input(
            "Что бы вы хотели купить?\n| меч: 25 урона, цена 200 |\n| моргенштерн: 50 урона, цена 500 |\n| копье: 40 урона, цена 400 |\n").lower().strip()
        if weapon == "меч":
            knight.damage += 25
            knight.withdraw(200)
            print("Отличный выбор!")
        elif weapon == "моргенштерн":
            knight.damage += 50
            knight.withdraw(500)
            print("Отличный выбор!")
        elif weapon == "копье":
            knight.damage += 40
            knight.withdraw(400)
            print("Отличный выбор!")
        else:
            print("такого оружия нет")

    elif buy == "доспехи":
        equipment = input(
            "Что бы вы хотели купить?\n| шлем: 40 защиты, цена 200 |\n| нагрудник: 120 защиты, цена 400 |\n| поножи: 80 защиты, цена 300 |\n| ботинки: 40 защиты, цена 200 |\n| наручи: 40 защиты, цена 200 |\n| щит: 60 защиты, цена 300 |\n").lower()
        if equipment == "шлем":
            knight.hp += 40
            knight.withdraw(200)
            print("Отличный выбор!")
        elif equipment == "нагрудник":
            knight.hp += 120
            knight.withdraw(400)
            print("Отличный выбор!")
        elif equipment == "поножи":
            knight.hp += 80
            knight.withdraw(300)
            print("Отличный выбор!")
        elif equipment == "ботинки":
            knight.hp += 40
            knight.withdraw(200)
            print("Отличный выбор!")
        elif equipment == "наручи":
            knight.hp += 40
            knight.withdraw(200)
            print("Отличный выбор!")
        elif equipment == "щит":
            knight.hp += 60
            knight.withdraw(300)
            print("Отличный выбор!")
        else:
            print("такой защиты нет")
    else:
        print("Такое купить нельзя")

print("Бой")
while dragon.hp > 0 and knight.hp > 0:  # проверка того, что у всех больше 0 здоровья
    action = randint(1, 2)  # для рандомного действия
    if action == 1:
        damage = randint(knight.damage - 100, knight.damage + 100)  # для слабого или критического удара
        dragon.hp -= damage
        if dragon.hp <= 0:
            dragon.hp = 0
        print(f"Вы нанесли дракону {damage} урона, у него осталось " + str(dragon.hp))
    elif action == 2:
        damage = randint(dragon.damage - 50, dragon.damage + 50)  # для слабого или критического удара
        knight.hp -= damage
        if knight.hp <= 0:
            knight.hp = 0
        print(f"Дракон нанес вам {damage} урона, у вас осталось " + str(knight.hp))

if dragon.hp == 0:  # выводим результат
    print("Ты выиграл! Принцесса спасена")
else:
    print("Выиграл дракон, попробуй еще раз")
