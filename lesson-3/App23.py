# 23.	Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]

import random
from random import randrange

N = int(input('Введите длину списка: '))
lst = [random.randrange(1, 10) for i in range(1, N + 1)]
print(f'Полученный список lst: {lst}')
arr = []

for i in range(len(lst)):
    last_el = - (i + 1)
    if lst[i] <= lst[last_el]:
        mult = lst[i] * lst[last_el]
        arr.append(mult)

print(f'Список произведения пар чисел списка lst: {arr}')
