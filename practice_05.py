"1"
dict = {"Alice": 25, "Bob": 30, "Charlie": 35}
name = input("Введите имя: ")
for k,v in dict.items():
  if k == name:
    print(name, v)


"2"
def sum_even(lst):
  lst2 = []
  sum = 0
  for i in lst:
    if int(i) > 0 and int(i) % 2 == 0:
      lst2.append(int(i))
  for j in lst2:
    sum += j
  return(sum)


lst = input("Введите ваши числа: ").split(", ")
sum_even(lst)



"3"
fruits_and_colors = {
    "apple": "red",
    "banana": "yellow",
    "mango": "yellow",
    "orange": "orange",
    "lemon": "yellow",
    "grape": "purple"
}

color = input("Введите цвет: ")
for k,v in fruits_and_colors.items():
  if v == color:
    print(k)


"4"
def invert(dict):
  for k,v in dict.items():
    return {v: k for k,v in dict.items()}

dict = {"a": 1, "b": 2, "c": 3}
invert(dict)


"5"
lst = ['apple','banana','orange','apple','apple','banana']

def count(lst):
  dict1 = {}
  for i in lst:
    if i in dict1:
      dict1[i] += 1
    else:
      dict1[i] = 1
  return(dict1)

#def sort(dict1):
#    return dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))

def sort(dict1):
    sorted_items = []
    while dict1:
        max_key = max(dict1, key=lambda k: dict1[k])
        sorted_items.append((max_key, dict1[max_key]))
        del dict1[max_key]
    return dict(sorted_items)


sort(count(lst))



"6"
people_info = {
    "Alice": {"age": 25, "city": "New York", "occupation": "Engineer"},
    "Bob": {"age": 30, "city": "Los Angeles", "occupation": "Designer"},
    "Charlie": {"age": 35, "city": "Chicago", "occupation": "Teacher"},
    "Diana": {"age": 28, "city": "Miami", "occupation": "Doctor"},
    "Ethan": {"age": 40, "city": "Seattle", "occupation": "Chef"},
    "Frank": {"age": 32, "city": "Atlanta", "occupation": "Lawyer"},
    "Gabriella": {"age": 29, "city": "San Francisco", "occupation": "Software Engineer"},
    "Harrison": {"age": 38, "city": "Denver", "occupation": "Architect"},
    "Isabella": {"age": 26, "city": "Washington D.C.", "occupation": "Journalist"},
    "Julian": {"age": 42, "city": "Miami", "occupation": "Musician"},
    "Kate": {"age": 31, "city": "Philadelphia", "occupation": "Nurse"},
    "Lucas": {"age": 36, "city": "Nashville", "occupation": "Businessman"},
    "Mia": {"age": 27, "city": "Atlanta", "occupation": "Artist"},
    "Natalie": {"age": 39, "city": "Portland", "occupation": "Writer"},
    "Oliver": {"age": 44, "city": "Minneapolis", "occupation": "Professor"},
    "Penelope": {"age": 33, "city": "San Diego", "occupation": "Marketing Manager"},
    "Quincy": {"age": 41, "city": "Nashville", "occupation": "Singer"},
    "Rachel": {"age": 34, "city": "Cleveland", "occupation": "Teacher"},
    "Sophia": {"age": 29, "city": "Nashville", "occupation": "Engineer"},
    "Tessa": {"age": 37, "city": "Miami", "occupation": "Lawyer"}
}

old_people = []
cities = []
occupations = []
people = []


def old(people_info, old_people):
  for k,v in people_info.items():
    if v["age"] > 30:
      print(k)


def city(people_info):
  for k,v in people_info.items():
      cities.append(v["city"])
  for i in set(cities):
    print(f"{i}: {cities.count(i)}")

def occupation(people_info):
  for k,v in people_info.items():
    occupations.append(v["occupation"])
  for j in set(occupations):
    for k,v in people_info.items():
      if v["occupation"] == j:
        people.append(k)
    print(j + ":", *people)
    people.clear()



print("Люди, которые старше 30 лет: ")
old(people_info, old_people)

print("Города и количество людей, проживающих там")
city(people_info)

print("Профессии и люди")
occupation(people_info)



"7"
# Добавление отзыва и оценки
def add(dict1):
    subject = input("Введите название предмета: ")  # Вводим все данные по предмету
    rating = int(input("Введите оценку: "))
    review = input("Введите отзыв: ")
    if subject in dict1.keys():  # Проверка предмета в словаре
        dict1[subject].append([rating, review])  # Если есть, то в список с отзывами добавляем новый
    else:
        dict1[subject] = [[rating, review]]  # Если нет, то создаем список
    return (dict1)


# Просмотр отзывов и оценок
def view(dict1):
    if dict1 == {}:  # Проверка того, есть ли в словаре предмет
        print("Нет предметов")
    else:
        subject = input("Введите название предмета: ")
        for k, v in dict1.items():
            if k == subject:
                for i, e in enumerate(v):  # Проходимся по списку с отзывами
                    print(f"{i + 1}) Оценка: ", end="")  # Выводим индекс и сам отзыв
                    print(*e, sep=", комментарий: ")
                else:
                    break
        else:
            print("Такого предмета нет")


# Удаление отзыва
def delet(dict1):
    if dict1 == {}:  # Проверка того, есть ли в словаре предмет
        print("Нет предметов")
    else:
        subject = input("Введите название предмета: ")
        for k, v in dict1.items():
            if k == subject:
                for i, e in enumerate(v):  # Проходимся по списку с отзывами
                    print(f"{i + 1}) Оценка: ", end="")  # Выводим индекс и сам отзыв
                    print(*e, sep=", комментарий: ")
                else:
                    break
        else:
            print("Такого предмета нет")
        index = int(input("Введите номер отзыва, который вы хотите удалить: "))
        for k, v in dict1.items():
            if k == subject:
                for i, e in enumerate(v):
                    if i + 1 == index:  # Сравниваем индекс, введенный пользователем и индекс предмета
                        v.pop(i)  # Удаляем отзыв из списка
                        print("Отзыв удален!")
                    else:
                        print("Индекс введен неправильно(")
                else:
                    break
        else:
            print("Такого предмета нет")


# Вычисление среднего балла по предмету
def ave(dict1):
    if dict1 == {}:  # Проверка того, есть ли в словаре предмет
        print("Нет предметов")
    else:
        sum = 0
        count = 0
        subject = input("Введите название предмета: ")
        for k, v in dict1.items():
            if k == subject:
                for e in v:  # Проходимся по списку
                    sum += e[0]  # Считаем сумму оценок
                    count += 1  # Считаем количество оценок
                else:
                    break
        else:
            print("Такого предмета нет")
        for k, v in dict1.items():
            if k == subject:
                print(f"Средняя оценка по предмету {subject}: {sum / count}")


dict1 = {}

while True:
    action = input(
        "Введите действие: Добавление отзыва и оценки / Просмотр отзывов и оценок / Удаление отзыва / Вычисление среднего балла по предмету / Выйти ").lower()
    if action == "добавление отзыва и оценки" or action == "отзыв":
        add(dict1)
    elif action == "просмотр отзывов и оценок" or action == "просмотр":
        view(dict1)
    elif action == "удаление отзыва" or action == "удаление":
        delet(dict1)
    elif action == "вычисление среднего балла по предмету" or action == "средний балл":
        ave(dict1)
    elif action == "выйти":
        print("Пока!")
        break
    else:
        print("Я не знаю такой команды(((((")
