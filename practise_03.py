"1"
#lst = []
#num = int(input("Сколько будет чисел? "))
#for i in range(0, num):
#  num = int(input("Введите ваше число: "))
#  lst.append(num)
#print(f"Сумма чисел: {sum(lst)}")
#print(f"Среднее арифм.: {(sum(lst)/len(lst))}")
#print(f"Максимальное значение: {max(lst)}")

lst_1 = []
sum = 0
count = int(input("Сколько будет чисел? "))
max = 1
for i in range(0, count):
  num = int(input("Введите ваше число: "))
  lst_1.append(num)
for l in lst_1:
  sum += l
ave = sum/count
for x in lst_1:
   if x > max:
       max = x

print(f"Сумма чисел: {sum}")
print(f"Среднее арифм.: {ave}")
print(f"Максимальное значение: {max}")


"2"
lst_2 = []
num = int(input("Сколько будет слов? "))
for i in range(0, num):
  word = str(input("Введите ваше слово: "))
  lst_2.append(word)

print(*reversed(lst_2))


"3"
import random


while True:
  action = input("С чем могу помочь? Сложение чисел / Подсказать фильм или музыку / Управлять списком дел / Выйти из чат-бота ").lower()
  if action == "сложение чисел" or action == "сложение":  # помогать складывать числа
    lst = []
    sum = 0
    count = int(input("Сколько будет чисел? "))
    max = 1
    for i in range(0, count):
      num = int(input("Введите ваше число: "))
      lst.append(num)
    for l in lst:
      sum += l
    print(sum)

  elif action == "подсказать фильм" or action == "фильм": #подсказывать фильмы
    movies = {1: "1+1", 2: "Интерстеллар", 3: "Побег из Шоушенка", 4: "Зеленая миля", 5: "Бойцовский клуб", 6: "Остров проклятых", 7: "Леон", 8: "Шрэк", 9: "Брат", 10: "Титаник"}# словарь, который можно изменять для того, чтобы расширять рекомендации
    movie = movies[round(random.randint(1, len(movies)))]
    print(f"Я бы посоветовал вам: {movie}")

  elif action == "подсказать музыку" or action == "музыка": #подсказывать музыку
    music = {1: "Pink Floyd - Time", 2: "Led Zeppelin - Stairway to Heaven", 3: "Queen - Bohemian Rhapsody", 4: "The Beatles - Let It Be", 5: "Nirvana - Smells Like Teen Spirit"}
    song = music[round(random.randint(1, len(music)))]
    print(f"Я бы посоветовал вам: {song}")

  elif action == "управлять списком дел" or action == "список дел" or action == "дела": #Управлять списком дел
      chores = []
      while True:
          print("Что бы вы хотели сделать со своим списком дел? Показать / Добавить задачу / Очистить / Выйти")
          action2 = input().lower()
          if action2 == "добавить задачу" or action2 == "добавить":
              print("Какую задачу вы бы хотели добавить?")
              task = input()
              chores.append(task)
              print("Ваш список дел на сегодня: ", end='')
              print(*chores, sep=", ")
              print("Хотели бы вы добавить в свой список больше задач?")
              task2 = input()
              while task2 == "да":
                  print("Напишите новую задачу:")
                  task = input()
                  chores.append(task)
                  print("Ваш список дел на сегодня: ", end='')
                  print(*chores, sep=", ")
                  print("Хотели бы вы добавить в свой список больше задач?")
                  task2 = input()
              if task2 == "нет" or task2 == "Нет":
                  print("Ваш список дел на сегодня: ", end='')
                  print(*chores, sep=", ")

          if action2 == "показать" or action2 == "показать список" or action2 == "показать список дел":
              if len(chores) == 0:
                  print(*chores, end='')
                  print("У вас нет задач")
              else:
                  print("ваш список дел:", end= " ")
                  print(*chores, sep=", ")

          if action2 == "очистить список" or action2 == "очистить":
              chores.clear()
              print("Ваш список дел очищен")
          if action2 == "выйти":
            break
  elif action == "выйти из чат-бота" or action == "выйти":
    print("Пока!")
    break

  else:
    print("У меня пока нет такого функционала((((")


"4"
import random
tools = ["камень", "ножницы", "бумага"]
tool = random.choice(tools)
user = str(input("Ваш предмет: "))
if tool == "камень" and user == "ножницы":
    print(f"Я выбрал {tool}")
    print("Я выиграл")
if tool == "ножницы" and user == "бумага":
    print(f"Я выбрал {tool}")
    print("Я выиграл")
if tool == "бумага" and user == "камень":
    print(f"Я выбрал {tool}")
    print("Я выиграл")
if tool == "камень" and user == "бумага":
    print(f"Я выбрал {tool}")
    print("Ты выиграл")
if tool == "ножницы" and user == "камень":
    print(f"Я выбрал {tool}")
    print("Ты выиграл")
if tool == "бумага" and user == "ножницы":
    print(f"Я выбрал {tool}")
    print("Ты выиграл")

# import random
# tools = ["Камень", "Ножницы", "Бумага"]
# tool = random.choice(tools)
# count = 0
# w = 0
# l = 0

# while (w < 3) and (l < 3):
#     for i in range(1, 7):
#         tool = random.choice(tools)
#         print(f"{i} раунд")
#         user = str(input("Ваш предмет: "))
#         if tool == "Камень" and user == "ножницы":
#             print(f"Я выбрал {tool}")
#             print("Я выиграл")
#             w += 1
#             print(f"Мой счёт: {w}")
#             print(f"Твой счёт: {l}")
#         if tool == "Ножницы" and user == "бумага":
#             print(f"Я выбрал {tool}")
#             print("Я выиграл")
#             w += 1
#             print(f"Мой счёт: {w}")
#             print(f"Твой счёт: {l}")
#         if tool == "Бумага" and user == "камень":
#             print(f"Я выбрал {tool}")
#             print("Я выиграл")
#             w += 1
#             print(f"Мой счёт: {w}")
#             print(f"Твой счёт: {l}")
#         if tool == "Камень" and user == "бумага":
#             print(f"Я выбрал {tool}")
#             print("Ты выиграл")
#             l += 1
#             print(f"Мой счёт: {w}")
#             print(f"Твой счёт: {l}")
#         if tool == "Ножницы" and user == "камень":
#             print(f"Я выбрал {tool}")
#             print("Ты выиграл")
#             l += 1
#             print(f"Мой счёт: {w}")
#             print(f"Твой счёт: {l}")
#         if tool == "Бумага" and user == "ножницы":
#             print(f"Я выбрал {tool}")
#             print("Ты выиграл")
#             l += 1
#             print(f"Мой счёт: {w}")
#             print(f"Твой счёт: {l}")
# if w == 3:
#     print("Я выиграл по итогу 3 раундов")
# elif l == 3:
#     print("Ты выиграл по итогу 3 раундов")


"5"
import random


lst = ["дерево", "стена", "карта", "небо", "поле"]
answer = random.choice(lst)
word_list = list('_' * len(answer))
print(*word_list, sep='')
att = 5

while att > 0:
    letter = input('Надо букву: ')
    if letter in answer:
        print('Есть такая буква')
        for i in range(len(answer)):
            if letter == answer[i]:
                word_list[i] = letter
                print(*word_list, sep='')
        if word_list.count("_") == 0:
            print("Ты выиграл")
            break
    else:
        print('Нет такой буквы!')
        att -= 1
        print(f'Осталось попыток: {att}')

else:
    print('Ты проиграл')
