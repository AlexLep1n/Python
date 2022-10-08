# 32.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

n = int(input('Введите длину списка: '))

lst = [randint(1, 10) for x in range(n)]
print(f'Полученный список: {lst}')

lst.sort()
print(f'Список после сортировки: {lst}')

lst_uniq = []
# Если надо плучить список, убрав дубль
# for i in range(len(lst)):
#     if lst[i] != lst[i - 1]:
#         lst_uniq.append(lst[i])

# Если надо плучить список, убрав числа, которые дублировались (1 вариант)
# for i in range(len(lst)):
#     if lst[i] != lst[i - 1] and lst[i] not in lst[i + 1:]:
#         lst_uniq.append(lst[i])

# Если надо плучить список, убрав числа, которые дублировались (1 вариант)
lst_uniq = [el for el in lst if lst.count(el) == 1]

print(f'Список неповторяющихся элементов: {lst_uniq}')
