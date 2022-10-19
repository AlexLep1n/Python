'''Создание светофора с помощью класса TrafficLight.'''
from time import sleep


class TrafficLight:
    '''Класс реализующий работу светофора'''
    __color = [('Красный', 7), ('Желтый', 2), ('Зеленый', 2)]

    def running(self):
        '''Переключает режим светофора. Вернет строку.'''
        for i in self.__color:
            print(i[0])
            sleep(i[1])
        return ('Можно ехать!')


obj = TrafficLight()
print(obj.running())
