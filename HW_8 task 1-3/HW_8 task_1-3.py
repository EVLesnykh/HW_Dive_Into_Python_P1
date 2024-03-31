# Исходные данные:

# Задание №1. Решить задачи, которые не успели решить на семинаре.

# Решение: Решение задач из семинара приложено к файлу ДЗ№8.

# Задание №2. Напишите функцию, которая получает на вход директорию и
# рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните
# в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.

# Решение: 

import csv
import json
import os
import pickle

__all__ = ['get_directory']

def get_directory(dir: str = '.') -> None:
    directory_info = []
    for root_dir, dirs, files in os.walk(dir):
        dir_size = 0
        for file in files:
            file_path = os.path.join(root_dir, file)
            file_size = os.path.getsize(file_path)
            dir_size += file_size
            directory_info.append({'path': file_path,
                             'root_dir': root_dir,
                             'type': 'file',
                             'size': file_size})
        directory_info.append({'path': root_dir,
                         'root_dir': os.path.dirname(root_dir),
                         'type': 'dir',
                         'size': dir_size})

    with open('directory_info.json', 'w', encoding='utf-8') as f_json:
        json.dump(directory_info, f_json, indent=2)

    headers = directory_info[0].keys()
    with open('directory_info.csv', 'w', encoding='utf-8') as f_csv:
        csv_writer = csv.DictWriter(f_csv, fieldnames=headers, dialect='excel',
                                    quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(directory_info)

    with open('directory_info.pickle', 'wb') as f_pickle:
        pickle.dump(directory_info, f_pickle)


if __name__ == '__main__':
    get_directory()

# Задание №3.Соберите из созданных на уроке и в рамках домашнего задания 
# функций пакет для работы с файлами разных форматов.

# Решение:
# См. файл __init__.py приложен к ДЗ№8.
