"1"
import requests


latitute_longitute = input("Введите координаты: ").split(", ") # Спрашиваем координаты
latitute_longitute = [float(i) for i in latitute_longitute] # Делаем из них список с числами
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitute_longitute[0]}&longitude={latitute_longitute[1]}&current=temperature_2m,apparent_temperature,precipitation,weather_code&timezone=GMT&forecast_days=1" # Изменяем ссылку
response = requests.get(url)  # отправка запроса
status_code = response.status_code  # код ответа
json = response.json()  # словарь ответа

for k, v in json['current'].items(): # Циклы для передачи значений переменным
    if k == 'time':
        time = f"{v[8:10]}.{v[5:7]}"
    elif k == 'precipitation' and v == 0.0:
        precipitation = 'осадков нет'
    elif k == 'precipitation' and v != 0.0:
        precipitation = 'осадки есть'
    elif k == 'apparent_temperature':
        temperature = f"{v}°C"
    elif k == 'weather_code' and (v != 45 or v != 43):
        fog = "тумана нет"
    elif k == 'weather_code' and (v == 45 or v == 43):
        fog = "туман есть"

print(f"Сегодня {time}, погода: {temperature}, {precipitation}, {fog}")


"2"
import requests


print("Список покемонов: ")  # Запрашиваем покемончиков
pokemons_url = "https://pokeapi.co/api/v2/pokemon?limit=20&offset=0"
response_pokemons = requests.get(pokemons_url)
json_pokemons = response_pokemons.json()
for json_value in json_pokemons['results']:  # Выводим покемончиков
    print(json_value['name'])

name = input("Введите имя покемона: ").lower()  # Запрашиваем покемончика
url = f"https://pokeapi.co/api/v2/pokemon/{name}"  # Изменяем ссылку
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
abilities = ", ".join(abilities_list)  # Делаем из списка строку для красивого вывода

print(f"Информация про покемона: имя: {name}, тип: {types}, вес: {weight}, рост: {height}, способности: {abilities}")


"3"
import requests, json


def posts(): # Функция для вывода всех постов
  url = "https://jsonplaceholder.typicode.com/posts"
  response = requests.get(url)  # отправка запроса
  json_data = json.dumps(response.json(), indent=4)
  print(json_data)


def ID(): # Функция для получения поста с помощью ID
  id = input("Введите ID: ")
  url = f"https://jsonplaceholder.typicode.com/posts/{id}"
  response = requests.get(url)  # отправка запроса
  json_data = json.dumps(response.json(), indent=4)
  print(json_data)


def info(): # Функция для вывода всей полезной информации с использованием прошлой функции
  id = input("Введите ID: ")
  url = f"https://jsonplaceholder.typicode.com/posts/{id}"
  response = requests.get(url)  # отправка запроса
  json = response.json()
  print(f"title: {response.json()['title']}\nbody: {response.json()['body']}")


posts()
ID()
info()


"4"
import requests, json


def new_post(): # Функция, которая принимает заголовок, содержимое и ID пользователя, выполняет POST-запрос для создания нового поста и возвращает информацию о созданном посте в формате JSON
  title = input("Введите новый заголовок: ").lower()
  body = input("Введите новое содержимое: ").lower()
  userId = input("Введите ID пользователя: ")
  data_new = { # Новая информация
      "userId": userId,
      "title": title,
      "body": body
  }
  url = f"https://jsonplaceholder.typicode.com/posts"
  response = requests.post(url, data = data_new) # метод post
  json = response.json()
  print(json)


def put_request(): # Функция, которая принимает ID поста, новый заголовок и новое содержимое, выполняет PUT-запрос и возвращает обновлённый пост в формате JSON
  title = input("Введите новый заголовок: ").lower()
  body = input("Введите новое содержимое: ").lower()
  id = int(input("Введите ID поста: "))
  data_new = { # Новая информация
      "title": title,
      "body": body
  }
  url = f"https://jsonplaceholder.typicode.com/posts/{id}"
  response = requests.put(url, data = data_new) # метод put
  json = response.json()
  print(json)


def delet(): # функция, которая принимает ID поста, выполняет DELETE-запрос и возвращает статус-код ответа
  id = int(input("Введите ID поста: ")) # Новая информация
  url = f"https://jsonplaceholder.typicode.com/posts/{id}"
  response = requests.delete(url) # метод delete
  status_code = response.status_code
  print(status_code)


new_post()
put_request()
delet()


"5"
import requests
from IPython.display import Image, display


def dogs_list(): # Функция для вывода собак
  print("Выберите породу собаки: ")
  url = "https://dog.ceo/api/breeds/list/all"
  response = requests.get(url)  # отправка запроса
  json = response.json()  # словарь ответа
  for i,e in enumerate(json['message']):
    print(i+1, e)



def photos(breeds):
  for i in breeds:
    url = f"https://dog.ceo/api/breed/{i}/images/random"
    response = requests.get(url)
    json = response.json()  # словарь ответа
    display(Image(url=json['message']))


dogs_list()
breeds = input("Введите пароды собак: ").split(", ")
photos(breeds)