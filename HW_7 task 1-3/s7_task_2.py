#Задание №2
#- Напишите функцию, которая генерирует псевдоимена.
#- Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
#обязательно должны быть гласные.
#- Полученные имена сохраните в файл.

import random
from random import randint

VOLEWELS = 'аеиоуяюёэы'     # гласные русские буквы
# CONSONANTS = (chr(char) for char in range(ord('а'), ord('я') + 1) if chr(char) not in VOLEWELS)   # согласные русские буквы в виде генератора, тогда print(*CONSONANTS)
CONSONANTS = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1) if chr(char) not in VOLEWELS])    # согласные русские буквы в виде списка, тогда print(CONSONANTS)


def make_random_name(amount_of_names: int):

    #
    count = 0
    all_names = []

    while count != amount_of_names:
        word_len = randint(4, 7)
        word = random.choices(VOLEWELS + CONSONANTS, k=word_len)
        if any(ch in VOLEWELS for ch in word):          # если есть хотя бы одна гласная в слове
            all_names.append(''.join(word).capitalize() + '\n')
            count += 1
    with open('task_2.txt', 'a', encoding='utf-8') as f:
        f.writelines(all_names)

if __name__ == '__main__':
    make_random_name(10)
    