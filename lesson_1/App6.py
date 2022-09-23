num = int(input("Введите день недели: "))

if num == 6 or num == 7:
    print("Это выходной день недели")
elif num <= 0 or num > 7:
    print("Такого дня недели не существует")
else:
    print("Это будний день недели")