'''
Реализация проекта расчета суммарного расхода ткани
на производство одежды.
'''
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    '''Реализует использование абстрактного метода.'''
    @abstractmethod
    def coat_fabric_consumption(self):
        pass

    @abstractmethod
    def suit_fabric_consumption(self):
        pass

    @abstractmethod
    def total_fabric_consumption(self):
        pass


class Clothes(AbstractClass):
    '''
    Класс реализующий рассчет суммарного рассчета ткани
    на производство одежды.
    '''

    def __init__(self, coat_v, suit_h):
        self.coat_v = coat_v
        self.suit_h = suit_h

    @property
    def coat_fabric_consumption(self):
        '''Рассчитывает расход ткани на пальто. Возвращает float.'''
        return f'Расход ткани на пальто: {round((self.coat_v / 6.5 + 0.5), 2)}'

    @property
    def suit_fabric_consumption(self):
        '''Рассчитывает расход ткани на костюм. Возвращает float.'''
        return f'Расход ткани на костюм: {round((2 * self.suit_h + 0.3), 2)}'

    @property
    def total_fabric_consumption(self):
        '''Рассчитывает общий расход ткани. Возвращает float.'''
        return (
            f'Общий расход ткани: {round(((self.coat_v / 6.5 + 0.5) + (2 * self.suit_h + 0.3)), 2)}'
        )


obj = Clothes(44.27, 177.50)
print(obj.coat_fabric_consumption)
print(obj.suit_fabric_consumption)
print(obj.total_fabric_consumption)
