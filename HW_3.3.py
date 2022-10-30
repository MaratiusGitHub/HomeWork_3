# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def subtraction_max_min(a):
    for i in range(len(a)):
        a[i] = round(a[i] % 1, 3)
    maxNum = a[0]
    minNum = a[0]
    for i in range(len(a)):
        if a[i] > maxNum and a[i] != 0:
            maxNum = a[i]
        elif a[i] < minNum and a[i] != 0:
            minNum = a[i]
    return maxNum - minNum


num = [1.1, 1.2, 3.1, 5, 10.01]
print(subtraction_max_min(num))
