x = int(input('Координата x = '))
y = int(input('Координата y = '))
if x != 0 and y != 0:
    if x > 0 and y > 0:
        print('Это 1 четверть')
    elif x < 0 and y > 0:
        print('Это 2 четверть')
    elif x < 0 and y < 0:
        print('Это 3 четверть')
    elif x > 0 and y < 0:
        print('Это 4 четверть')
