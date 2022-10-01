# 14.	Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# o	6782 -> 23
# o	0,56 -> 11


def sum_of_numbers(num):
    sum = 0
    for i in str(num):
        if i != "." and i != '-':
            sum += int(i)
    return sum

num = float(input("Введите вещественное число: "))
print(f"Сумма чисел равна: {sum_of_numbers(num)}")
