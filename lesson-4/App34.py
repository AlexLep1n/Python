# 34.	Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1	Файл :		2*x**2 + 4*x + 5 = 0
# 2	Файл :		4*x**2 + 7*x + 9 = 0
# 3	Файл: (содержит результат)	6*x**2 + 11*x + 14 = 0

from random import randint

k = 2
A_1 = randint(0, 100)
B_1 = randint(0, 100)
C_1 = randint(0, 100)
A_2 = randint(0, 100)
B_2 = randint(0, 100)
C_2 = randint(0, 100)
res_1 = f'{A_1}x^{k} + {B_1}x^{k - 1} + {C_1}x^{k - 2}'
res_2 = f'{A_2}x^{k} + {B_2}x^{k - 1} + {C_2}x^{k - 2}'
res_3 = f'{A_1 + A_2}x^{k} + {B_1 + B_2}x^{k - 1} + {C_1 + C_2}x^{k - 2}'
print(f"Первый многочлен: {res_1}")
print(f"Второй многочлен: {res_2}")
print(f"Сумма многочленов: {res_3}")


with open('file1.txt', 'w') as data:
    data.write(f'{res_1} = 0')

with open('file2.txt', 'w') as data:
    data.write(f'{res_2} = 0')

with open('file3.txt', 'w') as data:
    data.write(f'{res_3} = 0')
