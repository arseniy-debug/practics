"1"
def discount(price, amount, promocode):
  if 1000 < amount < 5000 and promocode != "SUPERDISCOUNT": #проверка цены и остутствия промокода
    discount = 5
    sum = price * amount * 0.95
    return(f"Ваша скидка: {discount}%, Итоговая сумма: {sum}")
  elif (1000 < amount < 5000) and (promocode == "SUPERDISCOUNT"): #проверка цены и наличия промокода
    discount = 10
    sum = price * amount * 0.9
    return(f"Ваша скидка: {discount}%, Итоговая сумма: {sum}")
  elif amount > 5000 and promocode != "SUPERDISCOUNT": #проверка цены и остутствия промокода
    discount = 15
    sum = price * amount * 0.85
    return(f"Ваша скидка: {discount}%, Итоговая сумма: {sum}")
  elif (amount > 5000) and (promocode == "SUPERDISCOUNT"): #проверка цены и наличия промокода
    discount = 20
    sum = price * amount * 0.8
    return(f"Ваша скидка: {discount}%, Итоговая сумма: {sum}")
  else: #если нет ни промокода, ни  нужного количества товара
    discount = 0
    sum = price * amount
    return(f"Ваша скидка: {discount}%, Итоговая сумма: {sum}")
sum = 0
price = int(input("Введите стоимость единицы товара: "))
amount = int(input("Введите количество товара: "))
promocode = str(input("Введите промокод: "))
print(discount(price, amount, promocode))


"2"
def positive(lst):
  lst2 = []
  for i in lst:
    if int(i) > 0:
      lst2.append(i)
  return(lst2)


lst = input("Введите ваши числа: ").split(" ")
answer_lst = positive(lst)
for j in answer_lst:
  print(j, end=' ')


"3"
def euclid(lst):
  a = int(lst[0])
  b = int(lst[1])
  while a != 0 and b != 0:
    if a > b:
      a -= b
    else:
      b -= a
  return(a)

lst = input("Введите ваши числа: ").split(" ")
print(euclid(lst))


"4"
#def c(lst):
#  set1 = set(lst)
#  return([f'{i}: {lst.count(i)}' for i in set1])

#lst = input("Введите ваши слова: ").split(" ")
#for j in c(lst):
#  print(j)




def c(lst):
  dict1 = {}
  for i in lst:
    if i in dict1:
      dict1[i] += 1
    else:
      dict1[i] = 1
  for k,v in dict1.items():
    print(f"{k}: {v}")


lst = list(input("Введите ваши слова: ").split(" "))
c(lst)




"5"
def an(lst):
  list1 = list(lst[0])
  list2 = list(lst[1])
  if len(list1) != len(list2):
    return False
  for i in list1:
    if i not in list2:
      return False
  return True

lst = input("Введите ваши слова: ").split(", ")
print(an(lst))


"6"
def encrypt(message, shift):
  new_message = []
  for i in range(len(message)):
    index = alphabet.index(message[i])+(shift % len(alphabet))
    if index > 25:
      index %= 26
    new_message.append(alphabet[index])
  return(new_message)


def decrypt(message, shift):
  new_message = []
  for i in range(len(message)):
    index = alphabet.index(message[i])-(shift % len(alphabet))
    if index > 25:
      index %= 26
    new_message.append(alphabet[index])
  return(new_message)


while True:
  action = input("Что вы хотите сделать? Зашифровать сообщение / Расшифровать сообщение / Выйти ").lower()
  if action == "зашифровать сообщение" or action == "зашифровать":
    message = str(input("Введите ваше сообщение: "))
    shift = int(input("Какой шаг? "))
    print(*encrypt(message, shift))
  elif action == "расшифровать сообщение" or action == "расшифровать":
    message = str(input("Введите ваше сообщение: "))
    shift = int(input("Какой шаг? "))
    print(*decrypt(message, shift))
  elif action == "выйти":
    print("Пока!")
    break
  else:
    print("Не получилось зашифровать сообщение / расшифровать сообщение")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


"7"
# Создание счета
def create(lst):
    name = input("Введите ваше имя: ")
    lst.append([name, 0])
    print(f"Был создан счет на имя {name}, ваш баланс 0 рублей.")
    return lst


# Внесение и снятие денег
def put(lst):
    if lst == []:
        print('Нет счетов')
    else:
        name = input("Введите ваше имя: ")
        for i in lst:
            if name == i[0]:
                print(f"Здравствуйте, {name}! У вас на балансе {i[1]} рублей.")
                action = input("Что вы хотите сделать? Внести деньги / Снять деньги ").lower()
                if action == "внести" or action == "внести деньги":
                    deposit = int(input("Введите сумму: "))
                    i[1] += deposit
                    print(f"Успешно! На вашем счету {i[1]} рублей.")
                    return (lst)
                else:
                    deposit = int(input("Введите сумму: "))
                    if deposit > i[1]:
                        print("У вас недостаточно средств")
                    else:
                        i[1] -= deposit
                        print(f"Успешно! На вашем счету {i[1]} рублей.")
                        return (lst)
        print("Такого счета нет")


# Проверить баланс
def balance(lst):
    if lst == []:
        print('Нет счетов')
    else:
        name = input("Введите ваше имя: ")
        for i in lst:
            if name == i[0]:
                print(f"Здравствуйте, {name}! У вас на балансе {i[1]} рублей.")
                return lst
        print("Такого счета нет")


# Переводить деньги между счетами
def transfer(lst):
    if lst == []:
        print('Нет счетов')
    else:
        if (len(lst)) < 2:
            print("Некому переводить")
        else:
            name_1 = input("C какого аккаунта вы хотите переводить деньги? ")
            for i in lst:
                if name_1 == i[0]:
                    deposit = int(input("Введите сумму: "))
                    if deposit > i[1]:
                        print("У вас недостаточно средств")
                    else:
                        i[1] -= deposit
                        print(f"Успешно! На счету осталось {i[1]} рублей.")
                        name_2 = input("На аккаунта вы хотите переводить деньги? ")
                        for i in lst:
                            if name_2 == i[0]:
                                i[1] += deposit
                                print(f"Успешно! На счету {i[1]} рублей.")
                                return lst
            print("Такого счета нет")


lst = []
transactions = []
ids = [i for i in range(1, 100)]
# lst = [[Имя, номер счета, сумма, ]]

while True:
    action = input("Введите действие: Создание счета / Изменение баланса / Проверить баланс / Переводить деньги / Выйти ").lower()
    if action == "создание счета" or action == "создание":
        lst = create(lst)
    elif action == "изменение баланса" or action == "изменение":
        put(lst)
    elif action == "проверить баланс" or action == "баланс":
        balance(lst)
    elif action == "переводить деньги" or action == "перевод":
        transfer(lst)
    elif action == "выйти":
        print("Пока!")
        break
    else:
        print("Не знаю такой команды")
