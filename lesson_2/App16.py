# Задайте список из n чисел последовательности 〖(1+1/n)〗^n  и выведите на экран их сумму.

num = int(input("Задайте список из n чисел: "))

list_of_num = [((1 + 1 / i) ** i) for i in range(1, num + 1)]
# чтобы видеть, что список формируется
print(list_of_num)

# функция сложения элементов списка
def sum_of_num(list):
    sum = 0
    for i in list:
        if i != ".":
            sum += round(i, 2)
    return sum


print(f"Сумма числе равна: {sum_of_num(list_of_num)}")
