# 18.	Реализуйте алгоритм перемешивания списка.
import random
from random import shuffle

n = int(input("Введите размер списка: "))

a = [random.randrange(1, 100) for i in range(0, n)]
print(f"Списко до перемешивания {a}")
random.shuffle(a)
print(f"Списко после перемешивания {a}")
