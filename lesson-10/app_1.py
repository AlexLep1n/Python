'''Реализация рассчета расчета массы асфальта с помощью класса Road.'''


class NonNegative:
    '''Класс, делающий атрибуты дескрипторами.'''

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Значения не могут быть отрицательными!')
        instance.__dict__[self.attr] = value

    def __set_name__(self, owner, attr):
        self.attr = attr


class Road:
    '''Класс, реализующий рассчет массы асфальта с применением дескрипторов.'''
    length = NonNegative()
    width = NonNegative()
    mass = NonNegative()
    thickness = NonNegative()

    def __init__(self, length, width, mass, thickness):
        '''Перегружает атрибуты класса и определяет заничения новых атрибутов.'''
        self.length = length
        self.width = width
        self.mass = mass
        self.thickness = thickness

    def calc_asphalt_mass(self):
        '''Рассчитывает массу асфальта. Возвращает int.'''
        result = self.length * self.width * self.mass * self.thickness
        return print(f'Масса асфальта = {int(result)} кг = {int(result / 1000)} т')


obj = Road(20, 5000, 25, 0.05)
print(obj.calc_asphalt_mass())
