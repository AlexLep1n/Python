'''
Реализация наследования 4 дочерних классов от класса Car.
Переопределение метода show_speed для классов TownCar и WorkCar.
'''


from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        '''Инициализация атрибутов'''
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        '''Сообщает о движении машины. Возращает строку.'''
        if self.speed != 0:
            return (f'Ваш {self.color} {self.name} едет.')

    def stop(self):
        '''Сообщает об остановке машины. Возращает строку.'''
        if self.speed == 0:
            return (f'Ваш {self.color} {self.name} остановился.')
        else:
            return ('Все в порядке.')

    def turn(self):
        '''Сообщает о направлении движения машины. Возращает строку.'''
        rand_turn = randint(1, 3)
        if rand_turn == 1:
            return (f'Ваш {self.color} {self.name} едет прямо.')
        elif rand_turn == 2:
            return (f'Ваш {self.color} {self.name} повернул направо.')
        else:
            return (f'Ваш {self.color} {self.name} повернул налево.')

    def show_speed(self):
        '''Сообщает о скорости машины. Возращает строку.'''
        return (f'Скорость {self.color} {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        '''Инициалирует наследование родительских атрибутов.'''
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        '''Переопределяет родительский метод для класса TownCar.'''
        if self.speed > 60:
            print(
                f'Вы превысили скоростной лимит!. Ваша скорость составила: {self.speed} км/ч.')
            is_police = True
            if is_police:
                print('Вас остановила полиция. :(')
                self.speed = 0
                return (f'Скорость {self.color} {self.name}: {self.speed} км/ч.')
        else:
            return (f'Скорость {self.color} {self.name}: {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        '''Инициалирует наследование родительских атрибутов.'''
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        '''Инициалирует наследование родительских атрибутов.'''
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        '''Переопределяет родительский метод для класса WorkCar.'''
        if self.speed > 40:
            print(
                f'Вы превысили скоростной лимит! Ваша скорость составила: {self.speed} км/ч.')
            is_police = True
            if is_police:
                print('Вас остановила полиция.')
                self.speed = 0
                return (f'Скорость {self.color} {self.name}: {self.speed} км/ч.')
        else:
            return (f'Скорость {self.color} {self.name}: {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        '''Инициалирует наследование родительских атрибутов.'''
        super().__init__(speed, color, name, is_police)


# Создание объектов классов TownCar, SportCar, WorkCar, PoliceCar
obj_town = TownCar(60, 'красный', 'Mustang', False)
obj_sport = SportCar(110, 'желтый', 'Porshe', False)
obj_work = WorkCar(50, 'черный', 'Ford', False)
obj_police = PoliceCar(40, 'синяя', 'полицейская Lada', False)

# Вывод результата работы методов для объекта класса TownCar
print(obj_town.go())
print(obj_town.turn())
print(obj_town.show_speed())
print(obj_town.stop())
print('\n')

# Вывод результата работы методов для объекта класса SportCar
print(obj_sport.go())
print(obj_sport.turn())
print(obj_sport.show_speed())
print(obj_sport.stop())
print('\n')

# Вывод результата работы методов для объекта класса WorkCar
print(obj_work.go())
print(obj_work.turn())
print(obj_work.show_speed())
print(obj_work.stop())
print('\n')

# Вывод результата работы методов для объекта класса PoliceCar
print(obj_police.go())
print(obj_police.turn())
print(obj_police.show_speed())
print(obj_police.stop())
