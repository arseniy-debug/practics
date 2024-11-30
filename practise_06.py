"1"
def twins(lst_1):
    ans = []
    for i in lst_1:
        if i not in ans:
            ans.append(i)
    for i in ans:
        print(i, end=" ")


lst_1 = input("Введите вашу строку: ").split(" ")
twins(lst_1)


"2"
def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def r_simple(lst_2):
    lower = int(lst_2[0])
    upper = int(lst_2[1])
    lst2 = []
    for i in range(lower, upper):
        if isprime(i):
            lst2.append(i)
    print(*lst2, sep=", ")


lst_2 = input("Введите ваши числа: ").split(", ")
r_simple(lst_2)


"3"
def unite(keys, values):
    dict = {}
    for i in range(len(values)):
        dict[keys[i]] = values[i]
    return dict


keys = ['a', 'b', 'c', 'e']
values = [1, 2, 3, 4]
unite(keys, values)


"4"
def sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return (sum)


def mean(numbers):
    len = 0
    for i in numbers:
        len += 1
    return ((sum(numbers)) / len)


def median(numbers):
    index = int(len(numbers) / 2)
    if len(numbers) % 2 != 0:
        return (numbers[index])
    else:
        return (((numbers[index - 1]) + numbers[index]) / 2)


def mode(numbers):
    max = 1
    mode = 0
    dict = {}
    for i in set(numbers):
        if numbers.count(i) > max:
            max = numbers.count(i)
            dict[max] = i
            print(dict)
    return (dict[max])


numbers = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict = {'mean': mean(numbers), 'median': median(numbers), 'mode': mode(numbers), 'sum': sum(numbers)}
print(dict)



"5"
def count(lst):
    ans = []
    count_letters = 0
    count_words = 0
    for i in lst:
        count_words += 1
        for j in i:
            count_letters += 1
        ans.append(count_letters)
        count_letters = 0
    print(f"Самое длинное слово с номером {ans.index(max(ans)) + 1}: {lst[ans.index(max(ans))]}")


lst = input("Введите вашу строку: ").split(" ")
count(lst)


"6"
# Добавление информации о студенте и его оценках
def add(dict1):
    student = input("Введите имя студента: ")  # Вводим все данные о студенте
    marks = input("Введите оценки студента: ").split(" ")
    if student in dict1.keys():  # Проверка ученика в словаре
        dict1[student] += marks  # Если есть, то в список с учениками добавляем новый
    else:
        dict1[student] = marks  # Если нет, то создаем список
    return (dict1)


# Подсчет среднего балла студента
def ave(dict1):
    if dict1 == {}:  # Проверка того, есть ли в словаре ученик
        print("Нет учеников")
    else:
        student = input("Введите имя студента: ")  # Вводим все данные о студент
        for k, v in dict1.items():
            if k == student:

                v = [int(i) for i in v]  # Переводим список со строками в список с числами
                print(f"Средний балл студента {student}: {sum(v) / len(v)}")
                break
        else:
            print("Такого ученика нет")


# Получение списка всех студентов с их средними баллами
def get(dict1):
    if dict1 == {}:  # Проверка того, есть ли в словаре ученик
        print("Нет учеников")
    else:
        for k, v in dict1.items():
            v = [int(i) for i in v]
            print(f"Ученик: {k}, средний балл: {sum(v) / len(v)}")


# Поиск студента по имени и вывод его оценок и среднего балла
def search(dict1):
    if dict1 == {}:  # Проверка того, есть ли в словаре ученик
        print("Нет учеников")
    else:
        student = input("Введите имя студента: ")  # Вводим все данные о студенте
        for k, v in dict1.items():
            v = [int(i) for i in v]
            if k == student:
                print(f"Ученик: {k}, средний балл: {sum(v) / len(v)}, оценки: ", end="")
                print(*v, sep=', ')  # Выводим список с оценками
                break
        else:
            print("Такого ученика нет")


dict1 = {}

while True:  # Бесконечный цикл
    action = input("Введите действие: Добавление информации / Подсчет среднего балла / Получение списка / Поиск студента по имени / Выйти ").lower()
    if action == "добавление информации" or action == "добавление":
        add(dict1)
    elif action == "подсчет среднего балла" or action == "средний балл":
        ave(dict1)
    elif action == "получение списка" or action == "список":
        get(dict1)
    elif action == "поиск студента по имени" or action == "поиск":
        search(dict1)
    elif action == "выйти":
        print("Пока!")  # Пока-пока!
        break
    else:
        print("Я не знаю такой команды")


"7"
import random


# Реализуйте функцию для представления вопросов, принятия ответов пользователей и предоставления обратной связи о том, являются ли ответы правильными или неправильными.
def counter(questions, USER):
    random.shuffle(questions)
    for i, e in enumerate(questions):
        print(f"{i + 1}) {e[0]} {e[2]} баллов")
    number = int(input("Введите номер вопроса: "))
    answer = input("Введите ответ: ").lower()
    for i, e in enumerate(questions):
        if number == (i + 1):  # Сравниваем номер, введенный пользователем и индекс вопроса
            if answer == e[1]:  # Если совпадают ответы
                USER += int(e[2])  # Прибавляем баллы
                del questions[i]  # Удаляем вопрос
                print("Ответ верный")
            else:
                print("Ответ неверный")
    return USER


# Реализуйте функцию добавления нового вопроса
def new_question(questions):
    question_new = input("Введите новый вопрос: ")
    answer_new = input("Введите ответ к этому вопросу: ")
    points_new = input("Введите баллы к этому вопросу: ")
    questions.append([question_new, answer_new, points_new])  # Добавляем новый вопрос


# Реализуйте функцию перемешивания вопросов, для отображения случайного вопроса
def mix(questions, USER):
    mixed_question = (random.choice([question[0] for question in questions]))  # Перемешиваем вопросы
    print(mixed_question)
    answer = input("Введите ответ: ")
    for i, e in enumerate(questions):
        if mixed_question == e[0]:
            if answer == e[1]:
                USER += int(e[2])
                print("Ответ верный")
            else:
                print("Ответ неверный")
    return USER


# Хранение данных о вопросах и ответах на них, а также баллов за каждый вопрос
questions = [
    ["Что носит дьявол в известном фильме?", "прада", "1"],
    ["Назовите страну с самой высокой продолжительностью жизни", "япония", "2"],
    ["В каком месте началась 1-ая мировая война?", "сараево", "3"],
    ["Сколько километров в одной миле?", "1.6", "4"],
    ["Назовите произведение Чернышевского, которое имеет название в виде вопроса", "что делать?", "5"]
]

USER = 0

while True:
    action = input("Введите действие: Ответить на вопрос / Добавить новый вопрос / Рандомный вопрос / Показать счет / Выйти и узнать результат ").lower()
    if action == "ответить на вопрос" or action == "ответить":
        USER = counter(questions, USER)
    elif action == "добавить новый вопрос" or action == "добавить":
        new_question(questions)
    elif action == "рандомный вопрос" or action == "рандом":
        USER = mix(questions, USER)
    elif action == "показать счет" or action == "счет":
        print(f"Ваш счет: {USER}")
    elif action == "выйти":
        print(f"У вас {USER} балл(а/ов)")
        print("Пока!")
        break
    else:
        print("Не знаю такой коменды")
