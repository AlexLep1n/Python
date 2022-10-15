'''Создание светофора с помощью класса TrafficLight.'''
from time import sleep


class TrafficLight:
    __color = 'цвет светофора'

    def __init__(self, *colors):
        '''Определяет заничения атрибутов при создании объекта класса.'''
        self.color_red = colors[0]
        self.color_yellow = colors[1]
        self.color_green = colors[2]

    def running(self):
        '''Переключает режим светофора. Вернет строку.'''
        print(f'{self.color_red} свет')
        sleep(7)
        print(f'{self.color_yellow} свет')
        sleep(2)
        print(f'{self.color_green} свет')
        sleep(2)
        return ('Можно ехать!')


obj = TrafficLight('Красный', 'Желтый', 'Зеленый')
print(obj.running())
