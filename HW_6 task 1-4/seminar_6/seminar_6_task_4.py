# Задача 4.Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# - 'Зимой и летом одним цветом',  ['ель', 'ёлка', 'сосна']

# Решение:
def riddle(question: str, answers: list, attempts: int) -> int:
    tries = 0
    print(question)
    while attempts:
        variant = input('Введите ответ: \n')
        if variant in answers:
            tries += 1
            print('Вы угадали!')
            return tries
        else:
            tries += 1
            print('Попробуйте снова!')
            attempts -= 1
    return -1


print(riddle("Отгадайте загадку:\nЗимой и летом одним цветом?",
             ['ель', 'ёлка', 'сосна'], 3))