'''Реализация рассчета расчета массы асфальта с помощью класса Road.'''


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width, mass, thickness):
        '''Перегружает атрибуты класса и определяет заничения новых атрибутов.'''
        self._length = length
        self._width = width
        self.mass = mass
        self.thickness = thickness

    def calc_asphalt_mass(self):
        '''Рассчитывает массу асфальта. Вазвращает int.'''
        result = self._length * self._width * self.mass * self.thickness
        return (f'Масса асфальта = {int(result)} кг = {int(result / 1000)} т')


obj = Road(20, 5000, 25, 0.05)
print(obj.calc_asphalt_mass())
