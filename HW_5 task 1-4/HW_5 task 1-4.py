# Исходные данные:

# Задание №1.Решить задачи, которые не успели решить на семинаре.
# -

# Задание №2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Решение:

import os

absolute_path = 'C:/Users/Екатерина/Desktop/git_education/HW_Dive_Into_Python_P1/HW_5 task 1-4.txt'

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {absolute_path} \nКортеж из пути: {fun(absolute_path)}')

# Задание №3. Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

# Решение:

names = ['Ирина', 'Владимир', 'Ольга']
salaries = [35000, 40000, 45000]
awards = ['10.25%', '5.25%', '6%']
print(f'исходные данные:\n{names}\n{salaries}\n{awards}')
print('Решение:')
print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})


# Задание №4. Создайте функцию генератор чисел Фибоначчи
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

# Решение:
a = int(input('Введите число: '))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fib(a)))
