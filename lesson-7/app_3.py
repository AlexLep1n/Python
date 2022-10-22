'''Реализация наследования класса Position от класса Worker. Получение полного имени сотрудника и дохода с учетом премии'''


class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def __init__(self, name, surname, position, _income, wage, bonus):
        '''Определяет заничения новых атрибутов и наследует атрибуты от класса родителя'''
        super().__init__(name, surname, position, _income)
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        '''Возвращает строку полного имени и должности сотрудника.'''
        return (f'Фамилия: {self.surname}\nИмя: {self.name}\nДолжность: {self.position}')

    def get_total_income(self):
        '''Возвращает зп сотрудика с учетом премии в виде целого числа.'''
        total_income = self._income.get('wage') + self._income.get('bonus')
        return (f'Доход с учетом премии: {total_income} тыс.р.')


obj = Position('Александр', 'Лепин', 'Frontend Developer', None, 150, 50)
print(obj.get_full_name())
print(obj.get_total_income())
print(f'Атрибут wage: {obj.wage}')
print(f'Атрибут bonus: {obj.bonus}')
print(f'Атрибут _income: {obj._income}')
print(f'Атрибут name: {obj.name}')
print(f'Атрибут surname: {obj.surname}')
print(f'Атрибут position: {obj.position}')
