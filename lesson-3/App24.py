# 24.	Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
from random import randrange

N = int(input('Введите длину списка: '))
# формируем список целых чисел
lst_int = [random.randrange(11, 100) for i in range(1, N + 1)]


# образуем список вещественных чисел из целочесленного списка
lst_float = []
count = 0

for i in lst_int:
    count += 1
    if count <= N:
        float_num = i / 10
        lst_float.append(float_num)

print(f'Полученный список вещественных чисел: {lst_float}')

# выделяем дробную часть и образуем новый список
lst_digit = []
for i in range(len(lst_float)):
    digit = lst_float[i] % 1
    lst_digit.append(round(digit, 1))

print(f'Дробная часть списка вещю чисел: {lst_digit}')

for i in range(len(lst_digit)):  # ищем максимальное и минимальное значение дробной
    max_digit = max(lst_digit)  # части списка lst_float
    min_digit = min(lst_digit)
    res = round((max_digit - min_digit), 2)

print(
    f'Разница между макс. и мин. значением дробной части элементов: {res}')
