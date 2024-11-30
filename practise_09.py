"1"
def unique(list_1, list_2):
  unique_elements = []
  for i in list_1:
    if i not in list_2:
      unique_elements.append(i)
    else:
      pass

  if unique_elements == []:
    print("нет уникальных элементов")
  else:
    unique_elements = set(unique_elements)
    print("Уникальные элементы: ")
    for j in unique_elements:
      print(j)


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

unique(a, b)


"2"
def adopt(tamagotchi, my_pets):  # функция для усыновления
    if tamagotchi != []:  # проверка на наличие питомцев
        for i, e in enumerate(tamagotchi):
            print(str(i + 1) + ") Тип питомца: " + e["type"] + ", имя: " + e["name"] + ", возраст: " + str(e["age"]))  # выводим список питомцев
        pet_name = input("Введите имя питомца, которого вы бы хотели усыновить: ").lower()
        pets_names = []
        for i in tamagotchi:
            pets_names.append(i["name"])
        if pet_name in pets_names:
            my_pets.append(tamagotchi[pets_names.index(pet_name)])  # добавляем питомца в список
            print("Вы успешно приютили питомца!")
            tamagotchi.remove(tamagotchi[pets_names.index(pet_name)])  # удаляем питомца из изначального списка
    else:
        print("Больше не осталось питомцев")
    return (my_pets)


def add(tamagotchi):
    print("Введите характеристики нового питомца:")
    name = input("Введите имя питомца: ").lower()
    type = input("Введите тип питомца (cat, dog, fish etc.): ").lower()
    age = input("Введите возраст питомца в годах: ").lower()
    tamagotchi.append({"name": name, "type": type, "age": age, "hunger": 50, "happiness": 50,"sleepiness": 50})  # характеристики нового питомца
    print("Вы успешно добавили питомца!")


def feed(my_pets):
    if my_pets != []:  # проверка наличия питомцев
        print("ваши питомцы: ")
        for i in my_pets:
            print(i["name"])  # выводим питомцев
        pet_name = input(
            "Введите имя животного, которое вы бы хотели покормить: ").lower()  # кормим конкретного питомца
        for i in my_pets:
            if pet_name == i["name"]:
                if i["hunger"] == 100:
                    print("У вас максимально сытый питомец")
                else:
                    i["hunger"] += 10
                    print("Успешно! теперь ваш питомец чуть-чуть более сытый")
            else:
                print("у вас нет такого питомца")
    else:
        print("У вас нет питомцев")


def play(my_pets):
    if my_pets != []:  # проверка наличия питомцев
        print("ваши питомцы: ")
        for i in my_pets:
            print(i["name"])  # выводим питомцев
        pet_name = input(
            "Введите имя животного, с которым вы бы хотели поиграть: ").lower()  # играем с конкретным питомцем
        for i in my_pets:
            if pet_name == i["name"]:
                if i["happiness"] == 100:
                    print("У вас максимально счастливый питомец")
                else:
                    i["happiness"] += 10
                    print("Успешно! теперь ваш питомец чуть-чуть более счастливый")
            else:
                print("у вас нет такого питомца")
    else:
        print("У вас нет питомцев")


def sleep(my_pets):
    if my_pets != []:  # проверка наличия питомцев
        print("ваши питомцы: ")
        for i in my_pets:
            print(i["name"])  # выводим питомцев
        pet_name = input(
            "Введите имя животного, которого вы бы хотели отправить спать: ").lower()  # укладываем спать определенного питомца
        for i in my_pets:
            if pet_name == i["name"]:
                if i["sleepiness"] == 100:
                    print("У вас максимально выспавшийся питомец")
                else:
                    i["sleepiness"] += 10
                    print("Успешно! теперь ваш питомец чуть-чуть более выспавшийся")
            else:
                print("у вас нет такого питомца")
    else:
        print("У вас нет питомцев")


my_pets = []

tamagotchi = [
    {"name": "myrzik", "type": "cat", "age": 4, "hunger": 50, "happiness": 50, "sleepiness": 50},
    {"name": "bobik", "type": "dog", "age": 7, "hunger": 50, "happiness": 50, "sleepiness": 50},
    {"name": "dori", "type": "fish", "age": 0.5, "hunger": 50, "happiness": 50, "sleepiness": 50}
]

while True:
    action = input("Что бы вы хотели сделать?\n| Добавить питомца |\n| Усыновить питомца |\n| Взаимодействие с питомцем |\n| Состояние питомцев |\n| Выйти |\n").lower()
    if action == "добавить питомца" or action == "Добавить":
        add(tamagotchi)
    elif action == "усыновить питомца" or action == "усыновить":
        adopt(tamagotchi, my_pets)
    elif action == "взаимодействие с питомцем" or action == "взаимодействие":
        if my_pets == []:
            print("У вас пока нет питомцев")
        else:
            interaction = input(
                "Выберите действие:\n| Покормить |\n| Поиграть |\n| Уложить спать |\n").lower()  # выбор взаимодействия с питомцем
            if interaction == "покормить":
                feed(my_pets)
            elif interaction == "поиграть":
                play(my_pets)
            elif interaction == "уложить спать" or interaction == "спать":
                sleep(my_pets)
            else:
                print("Я пока так не умею")
    elif action == "состояние питомцев" or action == "состояние":
        if my_pets == []:
            print("У вас пока нет питомцев")
        else:
            print("У вас есть: ")
            for i in my_pets:  # вывод питомцев
                print("Имя: " + i["name"] + ", тип питомца: " + i["type"] + ", возраст питомца: " + str(
                    i["age"]) + ", насколько сыт: " + str(i["hunger"]) + ", насколько счастлив: " + str(
                    i["happiness"]) + ", насколько бодр: " + str(i["sleepiness"]))
    elif action == "выйти":
        print("Пока, родитель")  # Пока-пока тамагочи
        break
    else:
        print("Я не знаю такой команды")


"3"
from random import randint


knight = {  # словарь персонажа
    "hp": 100,
    "damage": 100
}

dragon = {  # словарь дракона
    "name": "Ящерица",
    "damage": 100,
    "hp": 300
}

print("Где-то в 15 веке жил рыцарь, и завли его ...")  # мини-сюжет
name = str(input("Введите имя вашего рыцаря: "))
knight["name"] = name
print("И однажды дракон украл у рыцаря " + knight["name"] + " принцессу, и для того, чтобы получить ее назад, рыцарь " + knight["name"] + "должен победить дракона")
print("Для того, чтобы сражаться, нужно хорошенько подготовиться к бою, и для этого рыцарь " + knight["name"] + " отправился в таверну для покупки необходимого обмундирования и оружия")
gold = 1000
print("У вас есть 1000 золота, на которые вы можете потратить на оружие и доспехи")

while gold >= 200:  # цикл для покупки вещей
    buy = input("Что бы вы хотели купить?\n| Оружие |\n| Доспехи |\n").lower().strip()
    if buy == "оружие":
        weapon = input(
            "Что бы вы хотели купить?\n| меч: 25 урона, цена 200 |\n| моргенштерн: 50 урона, цена 500 |\n| копье: 40 урона, цена 400 |\n").lower().strip()
        if weapon == "меч":
            knight["damage"] += 25
            gold -= 200
            print("Отличный выбор!")
        elif weapon == "моргенштерн":
            knight["damage"] += 50
            gold -= 500
            print("Отличный выбор!")
        elif weapon == "копье":
            knight["damage"] += 40
            gold -= 400
            print("Отличный выбор!")
        else:
            print("такого оружия нет")
    elif buy == "доспехи":
        equipment = input(
            "Что бы вы хотели купить?\n| шлем: 40 защиты, цена 200 |\n| нагрудник: 120 защиты, цена 400 |\n| поножи: 80 защиты, цена 300 |\n| ботинки: 40 защиты, цена 200 |\n| наручи: 40 защиты, цена 200 |\n| щит: 60 защиты, цена 300 |\n").lower()
        if equipment == "шлем":
            knight["hp"] += 40
            gold -= 200
            print("Отличный выбор!")
        elif equipment == "нагрудник":
            knight["hp"] += 120
            gold -= 400
            print("Отличный выбор!")
        elif equipment == "поножи":
            knight["hp"] += 80
            gold -= 300
            print("Отличный выбор!")
        elif equipment == "ботинки":
            knight["hp"] += 40
            gold -= 200
            print("Отличный выбор!")
        elif equipment == "наручи":
            knight["hp"] += 40
            gold -= 200
            print("Отличный выбор!")
        elif equipment == "щит":
            knight["hp"] += 60
            gold -= 300
            print("Отличный выбор!")
        else:
            print("такой защиты нет")
    else:
        print("Такое купить нельзя")

print("Бой")
while dragon["hp"] > 0 and knight["hp"] > 0:  # проверка того, что у всех больше 0 здоровья
    action = randint(1, 2)  # для рандомного действия
    if action == 1:
        damage = randint(knight["damage"] - 100, knight["damage"] + 100)  # для слабого или критического удара
        dragon["hp"] -= damage
        if dragon["hp"] <= 0:
            dragon["hp"] = 0
        print(f"Вы нанесли дракону {damage} урона, у него осталось " + str(dragon["hp"]))
    elif action == 2:
        damage = randint(dragon["damage"] - 50, dragon["damage"] + 50)  # для слабого или критического удара
        knight["hp"] -= damage
        if knight["hp"] <= 0:
            knight["hp"] = 0
        print(f"Дракон нанес вам {damage} урона, у вас осталось " + str(knight["hp"]))

if dragon["hp"] == 0:  # выводим результат
    print("Ты выиграл! Принцесса спасена")
else:
    print("Выиграл дракон, попробуй еще раз")


"4"
import requests, random


def add():
  print("список покемонов:")
  pokemons_url = "https://pokeapi.co/api/v2/pokemon?limit=50&offset=0"
  response_pokemons = requests.get(pokemons_url)
  json_pokemons = response_pokemons.json() # Запрашиваем покемончиков
  for json_value in json_pokemons['results']:  # Выводим покемончиков
      print(json_value['name'])
  pokemon = input("Выберите покемонов, которых вы бы хотели обавить к себе в команду: ")
  pokemon_team.append(pokemon)
  return(pokemon_team)


def delete():
  if pokemon_team != []: # проверка наличия покемонов
    print("Ваши покемоны: ")
    for i in pokemon_team:
      print(i)
    pokemon = input("Введите имя покемона, которого вы хотели бы удалить")
    if pokemon in pokemon_team: # проверка наличия покемона
      pokemon_team.remove(pokemon)
      print("Вы успешно удалили покемона из команды")
    else:
      print("Такого покемона нет в команде")
  else:
    print("У вас нет покемонов")
  return(pokemon_team)


def info():
  if pokemon_team != []:
    for i in pokemon_team:
      url = f"https://pokeapi.co/api/v2/pokemon/{i}"  # Изменяем ссылку
      response = requests.get(url)  # отправка запроса тип: {types}, способности: {abilities}
      json = response.json()  # словарь ответа
      weight = json['weight']  # Берем значение веса
      height = json['height']  # Берем значение высоты
      types_list = []
      abilities_list = []
      for type in json['types']:  # Цикл для типов покемона
        types_list.append(type['type']['name'])
      for ability in json['abilities']:  # Цикл для способностей покемона
        abilities_list.append(ability['ability']['name'])
      types = ", ".join(types_list)  # Делаем из списка строку для красивого вывода
      abilities = ", ".join(abilities_list)
      print(f"Информация про покемона: имя: {name}, тип: {types}, вес: {weight}, рост: {height}, способности: {abilities}")
  else:
    print("У вас нет покемонов")


def find():
  if pokemon_team != []:
    pokemon = input("Введите имя покемона: ")
    if pokemon in pokemon_team:
      print("В команде есть такой покемон")
    else:
      print("В команде нет такого покемон")
  else:
    print("У вас нет покемонов")


def fight():
  pokemon_fight = []
  if pokemon_team != []:
    print("Ваши покемоны: ")
    for i in pokemon_team:
      print(i)
    if len(pokemon_team) == 1:
      print("У вас 1 покемон, нужно 2")
    else:
      pokemon_1 = input("Введите 1 покемона: ")
      if pokemon_1 in pokemon_team:
        pokemon_fight.append(pokemon_1)
        pokemon_2 = input("Введите 2 покемона: ")
        if pokemon_2 in pokemon_team:
          pokemon_fight.append(pokemon_2)
          print("Выиграл " + str(random.choice(pokemon_fight)))
        else:
          print("Такого покемона в команде нет")
      else:
        print("Такого покемона в команде нет")
  else:
    print("У вас нет покемонов")


pokemon_team = []

while True:
  action = input("Введите действие: \n| Добавить покемонов в свою команду |\n| Удалить покемонов из команды |\n| Просматривать информацию |\n| Найти покемона |\n| Тренировочный бой |\n| Выйти |\n").lower()
  if action == "добавить покемонов в свою команду" or action == "добавить":
    add()
  elif action == "удалить покемонов из команды" or action == "удалить":
    delete()
  elif action == "просматривать информацию" or action == "информация":
    info()
  elif action == "найти покемона" or action == "найти":
    find()
  elif action == "тренировочный бой" or action == "бой":
    fight()
  elif action == "выйти":
    print("До скорых встреч!")
    break
  else:
    print("Я не знаю такой команды")