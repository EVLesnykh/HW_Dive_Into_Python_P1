'''
Задание №1
Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
-второе и третье число являются ключами.
-первое число является значением для первого ключа.
-четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
'''

string = input('введите строку из четырёх или более целых чисел, разделённых символом “/”')
a, b, c, *d = string.split('/')
my_dict = {b:a, c:d}
my_dict1 = {b:a, c:tuple(d)}

print(my_dict)
print(my_dict1)


'''
Задание №2
- Самостоятельно сохраните в переменной строку текста.
- Создайте из строки словарь, где ключ — буква, а значение — код буквы.
- Напишите преобразование в одну строку.
'''

print({i: ord(i) for i in input('введите строку\n')})

'''
Задание №3
- Продолжаем развивать задачу 2.
- Возьмите словарь, который вы получили.
Сохраните его итераторатор.
- Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
'''

dict = {i: ord(i) for i in input('введите строку\n')}
dict_iter = iter(dict.items())

for i in range(5):
    print(next(dict_iter))


'''
Задание №4
- Создайте генератор чётных чисел от нуля до 100.
- Из последовательности исключите
числа, сумма цифр которых равна 8.
- Решение в одну строку.
'''


#1 вариант
# for i in range(0, 101, 2):
#     if sum(map(int, str(i))) != 8:
#         print(i)

print(*(i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8))

#2 вариант
print(*(i for i in range(0, 101, 2) if (i // 10 + i % 10) != 8))


'''
Задание №5
- Напишите программу, которая выводит
на экран числа от 1 до 100.
- При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
- Вместо чисел, кратных пяти — слово «Buzz».
- Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
- *Превратите решение в генераторное выражение.
'''

# for i in range (1, 101):
#     if i % 3 == 0 and i %5  == 0: # можно записать как if i % 3 == i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)

my_gen = ("fizzbuzz" if i % 3 == i % 5 == 0 else 'fizz' if i % 3 == 0  else "buzz" if i % 5 == 0 else i for i in range(1, 101))
print(*my_gen)
# for i in my_gen:
#     print(i)


'''Задание №6
- Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
- Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
- Для вывода результата используйте «принт»
без перехода на новую строку
'''

# 1 вариант
my_gen = (f'\n' if j == 11 else f' {j}*{i}={i * j:2d} ' for i in range(2, 10) for j in range(2, 12))
my_gen_1 = (f'\n' if j == 6 else f' {j}*{i}={i * j:2d} ' for i in range(2, 10) for j in range(2, 7))
my_gen_2 = (f'\n' if j == 11 else f' {j}*{i}={i * j:2d} ' for i in range(2, 10) for j in range(6, 12))
print(*my_gen)
print(*my_gen_1)
print(*my_gen_2)

#2 вариант
min_num = 2
max_num = 10
column = 4

[[print(f'{k:>} * {j:>2} = {k * j:>2}\n\n', end='') if (j == max_num and k == i + column - 1)
  else print(f'{k:>} * {j:>2} = {k * j:>2}\n', end='') if k == i + column - 1
else print(f'{k:>} * {j:>2} = {k * j:>2}\t\t', end='') for k in range(i, i + column)]
 for i in range(min_num, max_num, column) for j in range(min_num, max_num + 1)]


'''
Задание №7
- Создайте функцию-генератор.
- Функция генерирует N простых чисел,
начиная с числа 2.
- Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''

from typing import Generator

def primes(n: int) -> Generator:
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i


for num, i in enumerate(primes(100), start=1):
    print(f'{num} = {i}')

# Пример отличие return (обычной функции)от yield (функции-генератора)
from typing import Generator


def p(n) -> int:
    for i in range(n):
        return i

def p1(n) -> Generator:
    for i in range(n):
        yield i             # запоминает значение i и каждый раз при вызове функции начитнает соследующего значения i
        print('yield следующий')

gen = p1(10)        # кол значений не должно быть больше 10 иначе выбрасывает исключение при привышении кол генерации

for i in range(10):
    print('return ', p(10))
    print('yield   ', next(gen))
    
