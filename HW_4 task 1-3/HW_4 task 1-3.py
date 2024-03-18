# Исходные данные:

# Задание №1. Напишите функцию для транспонирования матрицы

# Решение:

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print("Исходная матрица:\n", matrix)

def matrix_transposition(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)

print("Транспонированная матрица:")
matrix_transposition(matrix)

# Задание №2.Напишите функцию принимающую на вход только ключевые параметры 
# и возвращающую словарь, где ключ — значение переданного аргумента, а
# значение — имя аргумента.Если ключ не хешируем, используйте его строковое представление.

# Решение:

def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(kwargs_to_dict(first_name = 'Екатерина', patronymic = 'Вячеславовна', last_name = 'Лесных'))

# Задание №3.Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте все операции поступления 
# и снятия средств в список.
# Примечание:
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

# Решение:

from datetime import date

bank = 0
count = 0
commission = 0.015
bonus = 0.03
tax = 0.01

def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + bonus  * bank
        print("Начислены проценты в размере: ", bonus  * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * commission < 30:
        bank -= 30
        print("Списаны проценты за cash: ", 30)
    elif cash * commission > 600:
        bank -= 600
        print("Списаны проценты за cash: ", 600)
    else:
        bank -= cash * commission
        print("Списаны проценты за cash: ", cash * commission)
    if count % 3 == 0:
        bank = bank + bonus  * bank
        print("Начислены проценты в размере: ", bonus  * bank)


def exit_bank():
    print("Будем рады Вас видеть снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50:\n"))
        if cash % 50 == 0:
            return cash

list_operation = []

while True:
    action = input("Выберите тип операции:\n1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * tax
            print("Списан налог на богатство: ", bank * tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("no money\n")
        if bank > 5_000_000:
            bank = bank - bank * tax
            print("Списан налог на богатство: ", bank * tax)
        print("Баланс = ", bank)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * tax
            print("Списан налог на богатство: ", bank * tax)
        print("Баланс = ", bank)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()
