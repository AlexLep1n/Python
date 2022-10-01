# 26.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input('Введите число: '))


def fib_poz(num):
    if num == 0:
        return 0
    elif num in [1, 2]:
        return 1
    else:
        return fib_poz(num - 1) + fib_poz(num - 2)


lst_r = []
for elem in range(N + 1):
    lst_r.append(fib_poz(elem))

print(f'Положительная часть чисел списка Фибоначчи: {lst_r}')


def fib_neg(num):
    if num in [1, 2]:
        return 1
    else:
        return fib_neg(num - 1) + fib_neg(num - 2)


lst_l = []
for elem in range(1, N + 1):
    lst_l.append(fib_neg(elem))

for i in range(len(lst_l)):
    if i % 2 != 0 and len(lst_l) != 0:
        lst_l[i] = - lst_l[i]

print(f'Отрицательная часть чисел списка Фибоначчи: {lst_l}')
lst_l_rev = lst_l[::-1]
lst_res = lst_l_rev + lst_r

print(f'Результат: {lst_res}')
