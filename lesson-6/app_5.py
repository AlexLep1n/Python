'''Пример использования функции zip.'''
# Данны спискок имен и список номеров пользователей,
# необходимо их соединить в массив кортежей
users_nums = [1, 2, 3, 4, 5]
users_names = ['Артем', 'Дмитрий', 'Марина', 'Екатерина', 'Максим']

users_lst = list(zip(users_nums, users_names))
print(users_lst)