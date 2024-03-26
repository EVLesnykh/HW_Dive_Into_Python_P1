# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры
# используйте генераторное выражение.

from sys import argv
from seminar_6_task1_2 import func

if __name__ == '__main__':
    min_val, max_val, triers = map(int, argv[1:])   # переводим в Int
    func(min_val, max_val, triers)

# Здесь также работает программа, что и в seminar_6_task1_2, только ввод осущствляется не через консоль, а через
# терминал (командную строку), в которой надо набрать команду python seminar_6_task_3.py 10 300 4
# где 10, 300, 4 - это min_val, max_val, triers
    