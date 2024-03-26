# Задача 5.Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# Решение:
dct = {"В чем сила: ": ['в правде', 'в деньгах', 'в силе'],
       "Не лает, не кусает, в дом не пускает": ['замок', 'охранник', 'собака']}

def riddle(question: str, answers: list, attempts: int) -> int:
    tries = 0
    print(question)
    while attempts:
        variant = input('Введите ответ:\n')
        if variant in answers:
            tries += 1
            print('Вы угадали!')
            return tries
        else:
            tries += 1
            print('Попробуйте снова!')
            attempts -= 1
    return -1


def riddle_storage(data):
    for k, v in data.items():
        riddle(k, v, 3)

riddle_storage(dct)