# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input('Введите число: '))
doubleNum = []

# Нахождение кол-ва чисел в двоичном формате
for i in range(a):
    if a - 2 ** i >= 0:
        doubleNum.append(0)
size = len(doubleNum)

# Преобразование десятичного числа в двоичное
for i in range(len(doubleNum)):
    size = size - 1
    if a >= 2 ** size:
        a -= 2 ** size
        doubleNum[i] = 1
    else:
        doubleNum[i] = 0

print(doubleNum)

