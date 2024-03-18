"""
Задание №1
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
*Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.


my_list = [1, 1, 2, 3]

#  короткое решение
# 1 вариант
print(list(set(my_list)))

# длинное решение
# 2 вариант
my_list = [1, 1, 2, 3]
my_set = {my_list[0]}
list_new = []
for i in my_list:
    my_set.add(i)
for i in my_set:
    list_new.append(i)
print(my_set)
print(list_new)

# 3 вариант
for i in my_list:
    if i not in list_new:
        list_new.append(i)

print(list_new)

Задание №2
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже""@
- Целое положительное число
- Вещественное положительное или отрицательное число
- Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
- Строку в нижнем регистре в остальных случаях

user = input('введите данные')

if user.isdigit():
    print(int(user))
elif user.find('.') !=-1 and user.replace('.', '').re""@ace('-', '').isdigit():
    print(float(user), 'dddd')
elif any([sym.isupper() for sym in user]):   # any[Tr""@, False, False -> True; all[True, True, True -> True;]
    print(user.lower())
else:
    print(user)


Задание №3
- Создайте вручную кортеж содержащий элементы разных ""@пов.
- Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа

import pprint
my_dict1 = {}
my_dict2 = {}

my_typle = (1, 2, "a", [1, 2, 3], 4.5, True, False, T""@e)
for i in my_typle:
    my_dict1.setdefault(type(i), []).append(i)       ""@  #верный результат (здесь значение словаря - список)
    my_dict2.setdefault(type(i), i)                  ""@ #неверный результат

pprint.pprint(my_dict1)                              ""@# для словарей очень удобно
print(my_dict1)                                      ""@  # верный результат
print(my_dict2)                                      ""@ # неверный результат

Задание №4
- Создайте вручную список с повторяющимися элементами""@
- Удалите из него все элементы, которые встречаются д""@жды.

my_list = [2, 1, 2, 4, 5, 4, 4, 6, 6]

for i in my_list:
    if my_list.count(i) == 2:
        my_list.remove(i)
        my_list.remove(i)

print(my_list)

Задание №5
- Создайте вручную список с повторяющимися целыми чис""@ми.
- Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
- Нумерация начинается с единицы.

my_list = [1, 2, 3, 5, 7, 8, 9, 10, 9, 8, 10]
new_list = []
for i in range(len(my_list)):
    if my_list[i] % 2 != 0:
        new_list.append(i + 1)
print([i + 1 for i in range(len(my_list)) if my_list[""@ % 2 != 0])          # короткий вариант записис (однострочник)
print(new_list)

Задание №6
Пользователь вводит строку текста. Вывести каждое сло""@ с новой строки.
-Строки нумеруются начиная с единицы.
- Слова выводятся отсортированными согласно кодировки""@nicode.
- Текст выравнивается по правому краю так, чтобы у са""@го длинного
слова был один пробел между ним и номером строки.


my_string = input('введите строку').split()

my_string.sort()
print(my_string)

longest = len(max(my_string, key=len))  # max возвращ""@т самую длиную строку
#longest = len(max(my_string))
for num, element in enumerate(my_string, 1):
    print(f'{num} {element:>{longest}}')

Задание №7
- Пользователь вводит строку текста.
- Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
- Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
- Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.

string = input("введите текст")
my_set = set(string)
my_dict_1 = {}
my_dict_2 = {}
my_dict_3 = {}
my_dict_4 = {}
# for i in range(len(string)):
#     my_set.add(string[i])

# с count
for i in my_set:
    #my_dict_1[i] = string.count(i)
    my_dict_1.setdefault(i, string.count(i))
print(my_dict_1)

# без count
count = 0
for i in my_set:
    for j in range(len(string)):
        if string[j] == i:
            count +=1
    my_dict_2[i] = count
    count = 0
print(my_dict_2)

# еще вариант
for char in string:
    my_dict_3[char] = my_dict_3.get(char, 0) + 1
print (my_dict_3)

# еще вариант
for i in string:
    my_dict_4[i] = string.count(i)
print (my_dict_4)

Задание №8
- Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
- Какие вещи взяли все три друга
- Какие вещи уникальны, есть только у одного друга
- Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
- Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.

diction = {"friend1": ('фонарик', 'тушенка', 'удочка', 'спальник', 'лопата', 'отвертка', 'топор'),
            "friend2": ('котелок', 'пила', 'удочка', 'спальник', 'лопата', 'фонарик'),
            "friend3": ('фонарик', 'палатка', 'удочка', 'спальник', 'лопата')
           }

set1 = set()
for k in diction:
    if not set1:
        set1 = set(diction[k])
    else:
        set1 &= set(diction[k])
print("какие вещи взяли все три друга:", set1)

my_tuple = diction.keys()

my_set = set()
for friend in my_tuple:
    my_set = set(diction[friend])

    for other_friends in [i for i in my_tuple if i != friend]:
        my_set = my_set - set(diction[other_friends])
    if my_set:
        print("Какие вещи есть у всех друзей кроме одного:", my_set)

for friend in my_tuple:
    to_remove = set(diction[friend])
    my_set = set()
    for other_friends in [i for i in my_tuple if i != friend]:
        if not my_set:
            my_set = set(diction[other_friends])
        else:
           my_set = my_set & set(diction[other_friends])

    my_set -= to_remove

    if my_set:
        print(f'{friend} не взял \'t {my_set}')
"""