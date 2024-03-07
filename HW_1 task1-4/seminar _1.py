# Задание №4. Решить в консоли
# Решите квадратное уравнение
# 5x2 - 10x - 400 = 0
# последовательно сохраняя переменные a, b, c, d, x1, x2

# Пишем в консоли
# python
# a = 5
# b = -10
# c = -400
# d = b ** 2 - 4 * a * c
# x1 = (-b + d ** 0.5) / (2 * a)
# x2 = (-b - d ** 0.5) / (2 * a)



# Задание №5
# Посчитайте сумму четных элементов от 1 до n исключая кратные e.
# Используйте while and if
# Попробуйте разные значения e and n


# Пишем в консоли
# python

# n = 101 
# e = 3
# sum = 0
# count = 0
# while count < n:
#    count += 2
#    if count % e ! = 0
#        s += count
# >>>s
# 1734

# Задание №6
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# В коде должен быть один input и print и учитывает год ввода григорианского календаря

# Решение:
#REFORM = 1582 # год ввода григорианского календаря, константа
#BIG_LEAP_YEAR = 400 # большой скачок года
#SMALL_LEAP_YEAR = 4 # маленький скачок года
#LARGE_NOT_BIG_YEAR = 100 # не високосный год
#MULTIPLE = 0 # для проверки на кратность
#year = int(input('Введите год в формате yyyy: '))
#if year < REFORM:
    #result = f'{year} год до ввода григорианского календаря, введите другой год'
#elif not year % BIG_LEAP_YEAR:
    #result = f'Год {year} високосный'
#elif not year % LARGE_NOT_BIG_YEAR:
     #result = f'Год {year} НЕ високосный'
#elif not year % SMALL_LEAP_YEAR:
     #result = f'Год {year} високосный'
#else:
    #result = f'Год {year} НЕ високосный'
#print(result)

# или
#year = int(input("Введите год: "))
#if year < 1582:
    #print("Не было еще григорианского календаря ")
#elif year % 4 != 0:
    #print("обычный год")
#elif year % 100 == 0 and year % 400 != 0:
    #print("обычный  год")
#else:
    #print("високосный год")

# Задание №7
#Пользователь вводит число от 1 до 999. Используя операции с числами
#сообщите что введено: цифра, двузначное число или трёхзначное число.
#Для цифры верните её квадрат, например 5 - 25
#Для двузначного числа произведение цифр, например 30 - 0
#Для трёхзначного числа его зеркальное отображение, например 520 - 25
#Если число не из диапазона, запросите новое число
#Откажитесь от магических чисел
#В коде должны быть один input и один print

#a = int(input("Введите число от 1 до 999 "))

#while True:
    #if 0 < a < 10:
        #result = a ** 2

    #elif 10 <= a < 100:
        #b = a // 10
        #c = a % 10
        #result = b * c

    #elif 100 <= a < 1000:
        #b = a // 100
        #c = a // 10 % 10
        #d = a % 10
        #result = d * 100 + c * 10 + b

    #else:
        #a = int(input("Вне диапозона, Введите число от 1 до 999"))
        #continue
    #break
#print(result)

# или
#LOWER_LIMIT = 1
#UPPER_LIMIT = 999
#ONE = 1
#TEN = 10
#HUNDRED = 100

#num = LOWER_LIMIT - ONE
#while num < LOWER_LIMIT or num > UPPER_LIMIT:
    #num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
#if num < TEN:
    #result = f'число {num} - цифра. Ее квадрат равен {num*num}'
#elif num < HUNDRED:
    #f_num = num // TEN
    #s_num = num % TEN
    #result = f'число {num} - двухзначное. Произведение цифр равно {f_num * s_num}'
#else:
    #f_num = num // HUNDRED
    #s_num = num // TEN % TEN
    #t_num = num % TEN
    #result = f'число {num} - трехзначное. Ее зеркальное отображение равно {t_num * HUNDRED + s_num * TEN + f_num}'
#print(result)

# Задание №8
#Нарисовать в консоли ёлку спросив
#у пользователя количество рядов.
#Пример результата:
#Сколько рядов у ёлки? 5
 #   *
 #  ***
 # *****
# *******
#*********

#SPACE = ' '
#STAR = '*'
#ONE = 1
#rows = int(input('Введите количество рядов ёлки: '))
#spaces = rows - ONE
#stars = ONE
#for i in range(rows):
  #print(spaces * SPACE + stars * STAR)
  #spaces -= ONE
  #stars += ONE + ONE

# или
#heigh = int(input("Введите количество рядов елки: "))
#i = 0
#while i < heigh:
    #j = 0

    #while j < heigh - 1 - i:
        #print(" ", end="")
        #j += 1
    #j = 0
    #while j < 2*i+1:
        #print("*", end="")
        #j += 1
    #print("")
    #i += 1

# Задание №9
#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

#for k in range(2):
    #for i in range (2,10):
        #for j in range(k*4 + 2, k*4+6):
            #print(f'{j:<2} * {i:<2} = {i * j: < 10}\t', end="")
        #print("")
    #print("")

# или 
#LOWER_LIMIT = 2
#UPPER_LIMIT = 11
#COLUMNS = 4

#for row in (LOWER_LIMIT, LOWER_LIMIT+COLUMNS):
     #for num_2 in range(LOWER_LIMIT, UPPER_LIMIT):
         #for num_1 in range(row, row + COLUMNS):
             #print(f'{num_1:>2} x {num_2: >2} = {num_1 * num_2:>2}', end='\t')
         #print()
     #print()
