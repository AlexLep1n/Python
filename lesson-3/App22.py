# 22.	Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
from random import randrange

n = int(input('Введите длину списка: '))
lst = [random.randrange(1, 10) for i in range(1, n + 1)]
print(lst)
nechet = []

for i in range(len(lst)):
    if i % 2 != 0:
        nechet.append(lst[i])
print(nechet)

res = 0
for i in nechet:
    res += i
print(res)
