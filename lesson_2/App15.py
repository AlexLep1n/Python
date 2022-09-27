# 15.	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# o	пусть N = 4, тогда [1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial_of_number(num):
    if num == 0:
        return 1
    else:
        return factorial_of_number(num - 1) * num


num = int(input("Введите число: "))
print(f"Факториал числа равен: {factorial_of_number(num)}")
