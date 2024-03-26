# Исходные данные:

# Задание №1.Решить задачи, которые не успели решить на семинаре.
# Решение: Решение задач из семинара приложено к файлу ДЗ№6.

# Задание №2. В модуль с проверкой даты добавьте возможность запуска
# в терминале с передачей даты на проверку.

# Решение:

import calendar
from sys import argv

def funcDate():
    text = (input('Введите дату в формате DD.MM.YYYY: '))
    text = text.split('.')
    month = int(text[1])
    days = calendar.monthrange(int(text[2]), int(text[1]))[1]
    if int(text[0]) <= days and int(text[1]) <= 12:
        print('Дата корректна!')
        a = input('')
        return True
    else :
        print('Дата некорректна!')
        a = input('')
        return False

def vys_Year(year):
    if calendar.monthrange(year, 2) == 29:
        return True
    else:
        return False

if __name__ == '__main__':
    funcDate()(argv[1:])        


# Задание №3. Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 
# можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 
# 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Решение:

N = 8
x, y = [0] * N, [0] * N

for i in range(N):
    enter = input(f'Введите координаты ферзя {i + 1} через пробел: ')
    x[i], y[i] = map(int, enter.split())

for i in range(N):
    for j in range(i + 1, N):
        if x[i] == x[j] or y[i] == y[j] or \
                abs(x[i] - x[j]) == abs(y[i] - y[j]):
            result = False
        else:
            result = True

print(result)

# Задание №4.Напишите функцию в шахматный модуль. Используйте генератор случайных
# чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки.

# Решение:

from random import randint

__all__ = ['set_queens', 'isCapture', 'show_success_cases']

N = 8
NUM_CASES = 4

x, y = [0] * N, [0] * N

def set_queens(n=N):
    for i in range(n):
        x[i], y[i] = randint(1, N), randint(1, N)
    return x, y

def isCapture(n=N):
    set_queens(n)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or \
                    abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
            else:
                return True

def show_success_cases(cases=NUM_CASES):
    success_cases = []
    while cases > 0:
        if isCapture():
            success_cases.append([*zip(x, y)])
            cases -= 1
    return success_cases


if __name__ == '__main__':
    for i, coord_list in enumerate(show_success_cases(), start=1):
        print(f'{i}: {coord_list}')
