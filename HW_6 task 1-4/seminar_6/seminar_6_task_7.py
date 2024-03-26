# Задание 7. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# Решение:

__all__ = ['true_data', 'my_data']

my_data = '01.02.2019'

def _year_funk(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Год високосный.')
        return False
    else:
        print('Год не високосный.')
        return True


def true_data(data):
    day, month, year = [int(el) for el in data.split('.')]
    if year > 9999 or month > 12:
        return False
    month_30 = (4, 6, 9, 11)
    month_31 = (1, 3, 5, 7, 8, 10, 12)
    if month in month_30:
        if 0 < day < 31:
            return True
        return False
    elif month in month_31:
        if 0 < day < 32:
            return True
        return False
    elif month == 2:
        if _year_funk(year):
            if 0 < day < 29:
                return True
            return False
        else:
            if 0 < day < 30:
                return True
            return False


print(true_data(my_data))
