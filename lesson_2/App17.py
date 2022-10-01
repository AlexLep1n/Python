# Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2
import math
import random
from random import randint

n = int(input("Введите число N: "))
list = [(i + 1) for i in range(-n - 1, n)]
print(list)

file_list = []
for i in range(1, n + 1):
    file_list.append(randint(1, len(list)))
print(file_list)


with open("file.txt", "w") as data:
    for file_item in file_list:
        data.write("%s\n" % str(file_item))

mult_num_from_poz = 1

with open("file.txt", "r") as data:
    for i in file_list:
        mult_num_from_poz *= list[int(i)]

print(mult_num_from_poz)
