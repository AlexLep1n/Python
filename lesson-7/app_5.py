'''
Создать три дочерних класса (Pen, Pencil, Handle) от родительского Stationery.
Для каждого из дочерних классов переопределить метод draw.
'''


class Stationery:
    def __init__(self, title):
        '''Инициализирует атрибут родительского класса.'''
        self.title = title

    def draw(self):
        '''Возвращает строку.'''
        return ('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        '''Инициализирует наследуемый атрибут.'''
        super().__init__(title)

    def draw(self):
        '''Возвращает строку.'''
        return (f'Запуск отрисовки {self.title}.')


class Pencil(Stationery):
    def __init__(self, title):
        '''Инициализирует наследуемый атрибут.'''
        super().__init__(title)

    def draw(self):
        '''Возвращает строку.'''
        return (f'Запуск отрисовки {self.title}.')


class Handle(Stationery):
    def __init__(self, title):
        '''Инициализирует наследуемый атрибут.'''
        super().__init__(title)

    def draw(self):
        '''Возвращает строку.'''
        return (f'Запуск отрисовки {self.title}.')


# Создание объектов классов Pen, Pencil, Handle
obj_origin = Stationery('канцелярская принадлежность')
obj_pen = Pen('ручкой')
obj_pencil = Pencil('карандашом')
obj_handle = Handle('маркером')

# Вывод результата работы метода draw для каждого из объектов
print(obj_origin.draw())
print(obj_pen.draw())
print(obj_pencil.draw())
print(obj_handle.draw())
