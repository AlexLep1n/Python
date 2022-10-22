'''Реализация класса Matrix.'''


class Matrix:
    '''Класс реализующий формирование матриц в понятном виде.
    А также складывающий их поэлементно.'''

    def __init__(self, *args):
        # Создает список из списков
        self.lst_of_arr = list(args)

    def __str__(self):
        # Функция map проходит по итерируемому объекту и вовращает объект map,
        # Метод join использует объект map и возвращает строки
        # с разделителем \n
        mtrx = '\n'.join(map(str, self.lst_of_arr))
        print(mtrx)
        # Метод replace заменяет выбранный элемент строки на указанный
        # Таким образом получаем матрицу в понятном виде
        mtrx = mtrx.replace('[', '').replace(']', '').replace(',', '')
        print(mtrx)
        return mtrx

    def __add__(self, other):
        # Суммирует по элементно массивы
        line_sum = []
        result_of_matrix_sum = []
        # Иттерируем список из списков поэлементно,
        # т.е. проходимся по каждой строке i
        for i in range(len(self.lst_of_arr)):
            # Иттерируем список в списке поэлементно,
            # т.е проходимся по каждому элементу j в строке i
            for j in range(len(self.lst_of_arr[i])):
                # Суммируем элементы строк матриц и добавляем их
                # в пустой массив line_sum
                line_sum.append(self.lst_of_arr[i][j] + other.lst_of_arr[i][j])
            result_of_matrix_sum.append(line_sum)
            # Обнуляем список суммы элементов j строк i
            # после добавления их в список result_of_matrix_sum
            line_sum = []
        # Преобразуем список списков result_of_matrix_sum
        # в приятный глазу вид
        result_of_matrix_sum = '\n'.join(map(str, result_of_matrix_sum))
        result_of_matrix_sum = result_of_matrix_sum.replace(
            '[', '').replace(']', '').replace(',', '')
        return result_of_matrix_sum


MTRX_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(f'Первая матрица:\n{MTRX_1}')
print()
MTRX_2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(f'Вторая матрица:\n{MTRX_1}')
print()
print(f'Сумма матриц:\n{MTRX_1 + MTRX_2}')
