"1"
print("Привет, мир!")


"2"
name = input("Введите свое имя")
print("Привет, " + name)


"3"
num = input("Введите число:")
if int(num) % 2 == 0:
  print("Ваше число четное!")
else:
  print("Ваше число нечетное!")


"4"
length = int(input("Введите длинну прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))
area = length*width
print(f"Площадь прямоугольника: {area}")


"5"
sum = 0
num = int(input("Сколько будет чисел? "))
for i in range(0, num):
  num = int(input("Введите ваше число "))
  sum += num
print(sum/count)
