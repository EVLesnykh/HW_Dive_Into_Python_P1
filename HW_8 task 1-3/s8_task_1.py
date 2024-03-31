# Задание №1 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл 
# с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
from pathlib import Path

def convert_to_json(path: Path) -> None:
    data = {}
    with(
        open(path, 'r', encoding='UTF-8') as f_read,
        open(path.stem + '.json', 'w', encoding='UTF-8') as f_write
    ):
        for line in f_read:
            name, number = line.split('|')
            data[name.capitalize()] = float(number)
        json.dump(data, f_write, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    convert_to_json(Path('result.txt'))
