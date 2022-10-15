'''Пример использования функции filter.'''
from random import randint

lst = [randint(1, 10) for el in range(1, 10)]
print(f"Начальный список: {lst}")

# Вариант решения без функции filter
# Создаем новый список только с четными элементами списка lst
new_lst = []
for el in lst:
    if el % 2 == 0:
        new_lst.append(el)

print(f"Список четных элеметов без применения filter: {new_lst}")

# Новое решение
lst = list(filter(lambda x: not x % 2, lst))
print(f'Список четных элеметов c применением filter: {lst}')
