#Задание №3
#- Напишите функцию, которая открывает на чтение созданные
#в прошлых задачах файлы с числами и именами.
#- Перемножьте пары чисел. В новый файл сохраните
#имя и произведение:
#- если результат умножения отрицательный, сохраните имя
#записанное строчными буквами и произведение по модулю
#- если результат умножения положительный, сохраните имя
#прописными буквами и произведение округлённое до целого.
#- В результирующем файле должно быть столько же строк,
#сколько в более длинном файле.
#- При достижении конца более короткого файла,
# возвращайтесь в его начало.

def whatever():
    with (open('task_1.txt', 'r', encoding='utf-8') as f_numbers,
          open('task_2.txt', 'r', encoding='utf-8') as f_names):
        numbers = f_numbers.readlines() #[' -945 | 875.661\n', '  375 | 269.492\n', ' -239 | 577.798\n', '  -74 | -659.06
        names = f_names.readlines()     #['Ащллжс\n', 'Еэижцп\n', 'Сглтих\n', 'Шдёг\n', 'Эжтбэт\n', 'Кксшолл\n', 'Ывэч\n',

    lines_to_write = []
    length_of_longest = max(len(numbers), len(names))

    for i in range(length_of_longest):
        num = numbers[i % len(numbers)]
        a, b = map(float, num.split('|'))       # a=-945   b=875.661
        mult = a * b

        name = names[i % len(names)]
        if mult >= 0:
            lines_to_write.append(f'{name.upper().rstrip()}; {round(mult)}\n')  # .rstrip() - убирает справа пробелы
        else:
            lines_to_write.append(f'{name.lower().rstrip()}; {abs(mult)}\n')

    with open ("task_3.txt", 'w', encoding='utf-8')as f:
        f.writelines(lines_to_write)

if __name__ == '__main__':
    whatever()
    