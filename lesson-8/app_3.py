'''Реализация программы работы с органическими клетками, состоящими из ячеек'''


class Cell:
    '''Реализует методы перегрузки арифметических операторов.'''

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        '''Метод возвращает строку значения объекта. Возвращает str.'''
        return f'{self.quantity}'

    def __add__(self, other):
        '''
        Метод перегружает результат суммы значений объектов.
        Возвращает str.
        '''
        return f'Сумма клеток равна: {Cell(self.quantity + other.quantity)}'

    def __sub__(self, other):
        '''
        Метод перегружает результат разности значений объектов.
        Возвращает str.
        '''
        if (self.quantity - other.quantity) > 0:
            return f'Разность клеток равна: {Cell(self.quantity - other.quantity)}'
        return 'Разность клеток не может быть отрицательна!'

    def __mul__(self, other):
        '''
        Метод перегружает результат умножения объектов.
        Возвращает str.
        '''
        return f'Умножение клеток равно: {Cell(self.quantity * other.quantity)}'

    def __truediv__(self, other):
        '''
        Метод перегружает результат умножения объектов.
        Возвращает str.
        '''
        if other.quantity != 0:
            return f'Деление клеток равно: {Cell(self.quantity / other.quantity)}'
        return 'Нельзя делить на ноль!'


cell_1 = Cell(10)
cell_2 = Cell(5)

# Сумма клеток
print(cell_1 + cell_2)
print()

# Разность клеток
print(cell_1 - cell_2)
print()

# Умножение клеток
print(cell_1 * cell_2)
print()

# Деление клеток
print(cell_1 / cell_2)
print()
