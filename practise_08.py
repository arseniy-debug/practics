"1"
import requests, json  # Импортируем библиотеки
from IPython.display import Image, display  # Импортируем библиотеку
import re  # Импортируем библиотеку


def APOD():  # Функция для картинки дня
    url = "https://api.nasa.gov/planetary/apod?api_key=XfsLhggOlzejqP9K5awunbTGtTGailwCbDNaiRU1"
    response = requests.get(url)  # отправка запроса
    json = response.json()  # Получение JSON
    display(Image(url=json['url']))  # Вывод картинки
    print(json['explanation'])  # Вывод описания


def mars_rover_photos():
    image_lst = []
    date = input("Напишите дату формата YYYY-MM-DD от 2012-08-06: ")
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(pattern, date):  # Проверка формата даты
        url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key=XfsLhggOlzejqP9K5awunbTGtTGailwCbDNaiRU1"
        response = requests.get(url)  # отправка запроса
        json = response.json()  # Получение JSON
        if json['photos'] == []:  # Проверка наличия фото
            print("Марсоход не делал в этот день фотографии")
        else:
            camera = input(
                "Введите камеру, с которй хотите получить фотографии: FHAZ, RHAZ, MAST, CHEMCAM, MAHLI, MARDI, NAVCA: ")
            for i in json['photos']:  # Находим ссылки на картинки и добавляем в заранее созданный список
                if i['camera']['name'] == camera:
                    image_lst.append(i['img_src'])
                elif i['camera']['name'] != camera:
                    pass
                else:
                    break
        for i in image_lst:
            display(Image(url=i))  # Выводим фотографии
    else:
        print("Строка не соответствует формату даты YYYY-MM-DD.")


def NEO():
    list = []
    date = input("Напишите дату формата YYYY-MM-DD: ")
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(pattern, date):  # Проверка формата даты
        url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key=XfsLhggOlzejqP9K5awunbTGtTGailwCbDNaiRU1'
        response = requests.get(url)  # отправка запроса
        json = response.json()  # Получение JSON
        print(json["near_earth_objects"].keys())
        for i in json["near_earth_objects"][date]:
            if i["is_potentially_hazardous_asteroid"] == False:  # Проверка на опасность
                print(f"Имя: {i['name']}, потенциальная опасность: нет, примерные размеры: " + str(
                    i["estimated_diameter"]["kilometers"][
                        "estimated_diameter_max"]) + " км диаметром")  # Выводим информацию про объект
            else:
                print(f"Имя: {i['name']}, потенциальная опасность: есть, примерные размеры: " + str(
                    i["estimated_diameter"]["kilometers"]["estimated_diameter_max"]) + "км диаметром")
    else:
        print("Строка не соответствует формату даты YYYY-MM-DD.")


def space_weather():
    url_GST = f'https://api.nasa.gov/DONKI/GST?api_key=XfsLhggOlzejqP9K5awunbTGtTGailwCbDNaiRU1'
    url_solar_flare = f'https://api.nasa.gov/DONKI/FLR?api_key=XfsLhggOlzejqP9K5awunbTGtTGailwCbDNaiRU1'
    response_GST = requests.get(url_GST)  # отправка запроса
    json_GST = response_GST.json()
    response_solar_flare = requests.get(url_solar_flare)  # отправка запроса
    json_solar_flare = response_solar_flare.json()
    print("Последняя информация про геомагнитные бури:")
    print("kp индексы:")
    for i in json_GST:
        dict_1 = i
    for j in dict_1["allKpIndex"]:
        print(j["kpIndex"])  # Выводим kp индексы
    print("Последняя информация про солнечные вспышки:")
    for i in json_solar_flare:
        if i['note'] == '':  # Проверка на наличие записей ученых
            print("Тип вспышки: " + i["classType"])
            print("Время начала вспышки: " + i["beginTime"][:10] + " в " + i["beginTime"][11:16])
            print("Время окончания вспышки: " + i["endTime"][:10] + " в " + i["endTime"][11:16])
            print("Пик вспышки: " + i["peakTime"][:10] + " в " + i["peakTime"][11:16])
            print("Записей нет")
            print(" ")
        else:
            print("Тип вспышки: " + i["classType"])
            print("Время начала вспышки: " + i["beginTime"][:10] + " в " + i["beginTime"][11:16])
            print("Время окончания вспышки: " + i["endTime"][:10] + " в " + i["endTime"][11:16])
            print("Пик вспышки: " + i["peakTime"][:10] + " в " + i["peakTime"][11:16])
            print("Записи: " + i['note'])
            print(" ")


while True:  # Бесконечный цикл
    action = input(
        "Выберите действие: | Астрономическая картинка дня |\n| Фотографии с марсохода |\n| Объекты, сближающиеся с Землей |\n| Данные о космической погоде |\n| Выход |\n").lower()  # Ввод действия
    if action == "астрономическая картинка дня":  # Проверяем ввод пользователя
        APOD()
    elif action == "фотографии с марсохода":  # Проверяем ввод пользователя
        mars_rover_photos()
    elif action == "объекты, сближающиеся с землей":  # Проверяем ввод пользователя
        NEO()
    elif action == "данные о космической погоде":  # Проверяем ввод пользователя
        space_weather()
    elif action == "выход":  # Проверяем ввод пользователя
        print("До скорых встреч!")  # Пока-пока
        break  # Прекращаем цикл, если пользователь хочет выйти
    else:
        print("Не знаю такой команды(")  # Обрабатываем неправильный ввод пользователя


"2"
import requests, json  # Импортируем библиотеки
from IPython.display import Image, display  # Импортируем библиотеку


next_page = 0
total_limit = 0


# извлекает список произведений искусства из API
def list():
    global next_page, total_limit # для сохранения текущей страницы
    page = int(input("Введите номер страницы: "))
    next_page = page
    limit = input("Введите, сколько названий картин будет в одной странице: ")
    total_limit = limit # для сохранения количества картин
    url = f'https://api.artic.edu/api/v1/artworks?page={page}&limit={limit}'
    response = requests.get(url)  # отправка запроса
    json = response.json()  # Получение JSON
    for i, e in enumerate(json["data"]): # Выводим картины
        print(f"{i + 1}) " + e['title'] + " от " + e["artist_display"] + ", id художника: " + str(e["artist_id"]))
    next()


def change(next_page): # Функция, показывающая другую страницу
    url = f'https://api.artic.edu/api/v1/artworks?page={next_page}&limit={total_limit}'
    response = requests.get(url)  # отправка запроса
    json = response.json()  # Получение JSON
    for i, e in enumerate(json["data"]):
        print(f"{i + 1}) " + e['title'] + " от " + e["artist_display"] + ", id художника: " + str(e["artist_id"]))
    next()


def next(): # Функция, меняющая страницы
    global next_page
    new = input("Хотите перейти на другую страницу? ").lower()
    if new == "нет":
        return 0
    elif new == "да":
        next = input("Вы хотите перейти на следующую страницу или предыдущую? ")
        if next == "следующая":
            next_page += 1
            change(next_page)
        elif next == "предыдущая":
            next_page -= 1
            change(next_page)
    return next_page


# фильтрует список произведений искусства на основе имени указанного художника
def artist():
  artists_name = ''
  artist = input("Введите id художника: ")
  url = f'https://api.artic.edu/api/v1/artworks?filter[artist_id]={artist}'
  response = requests.get(url)  # отправка запроса
  json = response.json()  # Получение JSON

  url_2 = f'https://api.artic.edu/api/v1/artists/{artist}'
  response_2 = requests.get(url_2)  # отправка запроса
  json_2 = response_2.json()  # Получение JSON
  for i in json['data']:
    if i['artist_title'] == json_2['data']['title']: # сравнение нужного имени со всеми в списке
      print(i['title'] + " id картины: " + str(i['id']))


# отображает названия работ для пользователя и позволяет ему выбрать одну из них, введя соответствующий номер
def artwork():
    artwork_id = input("Введите id картины: ")
    url = f'https://api.artic.edu/api/v1/artworks/{artwork_id}'
    response = requests.get(url)  # отправка запроса
    json = response.json()  # Получение JSON
    print("Название картины: " + json['data']['title']) # выводим все данные про картину
    print("Исполнитель картины: " + str(json['data']['artist_title']))
    print("Дата начала написания картины: " + str(json['data']['date_start']))
    print("Дата окончания написания картины: " + str(json['data']['date_end']))
    print("Носитель: " + json['data']["thumbnail"]["alt_text"])


# основную функцию, которая управляет выборкой произведений и взаимодействием с пользователем
while True:
  action = input("Введите действие: |Показать страницу с картинами|\n|Фильтровать список картин по художнику|\n|Информация про картину|\n|Выйти|\n").lower()
  if action == "показать страницу с картинами":
    list()
  elif action == "фильтровать список картин по художнику":
    artist()
  elif action == "информация про картину":
    artwork()
  elif action == "выйти":
    print("До скорых встреч!")
    break
  else:
    print("Я не знаю такой команды.")


"4"
import requests  # Импортируем библиотеки
from IPython.display import Image, display  # Импортируем библиотеку
from random import choice # Импортируем библиотеку


def dog():
  dogs_list = []
  input("Насколько вы грустные от 1 до 10: ")
  url = 'https://random.dog/woof.json'
  for i in range(1, 11):
    response = requests.get(url)  # отправка запроса
    json = response.json()  # Получение JSON
    dogs_list.append(json["url"])
  print("Вот вам собачки, не грустите :)")
  for i in dogs_list:
    display(Image(url=i))


def random():
  lst = [i for i in range(0, 4)] # Генератор списков
  random_list = ['http://numbersapi.com/random/trivia?json', 'http://numbersapi.com/random/year?json', 'http://numbersapi.com/random/date?json', 'http://numbersapi.com/random/math?json']
  num = choice(lst) # Ищем случайное число
  url = random_list[num] # Ищем случайную ссылку
  response = requests.get(url)  # отправка запроса
  json = response.json()  # Получение JSON
  print(json["text"])


def math():
  num = int(input("Введите число: "))
  url = f"http://numbersapi.com/{num}/math?json"
  response = requests.get(url)  # отправка запроса
  json = response.json()  # Получение JSON
  print(json["text"])


def trivia():
  num = int(input("Введите число: "))
  url = f"http://numbersapi.com/{num}?json"
  response = requests.get(url)  # отправка запроса
  json = response.json()  # Получение JSON
  print(json["text"])


def history():
  num = input("Введите число формата MM/DD: ")
  url = f"http://numbersapi.com/{num}/date?json"
  response = requests.get(url)  # отправка запроса
  json = response.json()  # Получение JSON
  print(json["text"])


while True:
  action = input("Введите действие: |Рандомный факт|\n|Математический факт|\n|Интересный факт|\n|Исторический факт|\n|Если вам грустно|\n|Выйти|\n").lower()
  if action == "рандомный факт":
    random()
  elif action == "математический факт":
    math()
  elif action == "интересный факт":
    trivia()
  elif action == "исторический факт":
    history()
  elif action == "если вам грустно" or action == "грустно":
    dog()
  elif action == "выйти":
    print("До скорых встреч!")
    break
  else:
    print("Я не знаю такой команды.")