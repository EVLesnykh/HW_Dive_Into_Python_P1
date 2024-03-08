#1. Решить задачи, которые не успели решить на семинаре.
# Файл решения задач на семинаре приложен к ДЗ.

#2. Напишите программу, которая получает целое число и возвращает его
#шестнадцатеричное строковое представление.
#Функцию hex используйте для проверки своего результата.

# Решение:
number = int(input("Введите целое число: "))
base = int(input("Введите основание системы счисления, в которую надо перевести число: "))
num = abs(number)
number_new = ''

str_ = "0123456789abcdef"
while num:
    num_char = str_[num % base]

    number_new = num_char + number_new
    num //= base
    print(f'{num_char = }   {num = }   {number_new = }')


if number < 0:
    number_new = "-" + number_new
if number == 0:
    number_new = "0"

print(f'Число {number} в {base}-ой системе счисления -> {number_new}')
print(f'Проверка: число {number} в 16-ой системе счисления -> {hex(number)}')

#3. Напишите программу, которая принимает две строки вида “a/b” - 
#дробь с числителем и знаменателем.Программа должна возвращать сумму 
#и произведение* дробей. Для проверки своего кода используйте модуль fractions.

# Решение:

from fractions import Fraction

def calculate_fraction_operations(fraction1, fraction2):
    # Разделяем строки дробей на числитель и знаменатель
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))
    # Создаем объекты Fraction для каждой дроби
    fraction_obj1 = Fraction(numerator1, denominator1)
    fraction_obj2 = Fraction(numerator2, denominator2)
    # Выполняем операции с дробями
    sum_fraction = fraction_obj1 + fraction_obj2
    product_fraction = fraction_obj1 * fraction_obj2
    return sum_fraction, product_fraction

# Получаем две строки с дробями от пользователя
fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")
# Выполняем вычисления
sum_result, product_result = calculate_fraction_operations(fraction1, fraction2)
# Выводим результаты
print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)
