"""Программа, вернет сумму элементов, стоящих стоящих на нечётной позиции."""
# 22.	Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from functools import reduce
from random import randint


n = int(input('Введите длину списка: '))
lst = [randint(1, 10) for i in range(1, n + 1)]
print(lst)

# Старое решение:

# nechet = []
# for i in range(len(lst)):
#     if i % 2 != 0:
#         nechet.append(lst[i])
# print(nechet)

# res = 0
# for i in nechet:
#     res += i
# print(res)

# Новое решение:

# Решение с применением lc:
lst = [lst[i] for i in range(len(lst)) if i % 2 != 0]
print(lst)

# Часть решения с применением функции reduce и lambda:
result = reduce(lambda x, y: x + y, lst)
print(result)
