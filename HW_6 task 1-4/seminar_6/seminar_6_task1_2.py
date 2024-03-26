# Задача 1. Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами.
# (3-7 строк импорта).

"""
from decimal import Decimal as D
from random import randint as rnd
from math import sqrt as sq
from sys import argv as arguments
from fractions import Fraction as F
"""

# Задача 2. Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.


from random import randint

def func(min_val, max_val, tries):

    num = randint(min_val, max_val)
    guess_num = 0
    count = 1
    while guess_num != num:
        if count > tries:
            print("Попытки закончились, Вы проиграли(((")
            break
        print("Попытка №", count)
        guess_num = int(input("Введите число: "))
        if guess_num > num:
            print("Число меньше!")
        elif guess_num == num:
            print("Вы угадали!")
        else:
            print("Число больше!")
        count += 1

if __name__ == '__main__':  
    func(50, 500, 2)
