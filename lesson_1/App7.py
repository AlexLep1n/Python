# 7.	Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
#  Где V - or, ⋀ - and, ¬ - not.
print("x y z  f1  f2")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f1 = not (x or y or z)
            f2 = not x and not y and not z
            f1 == f2
            print(x, y, z, f1, f2)
