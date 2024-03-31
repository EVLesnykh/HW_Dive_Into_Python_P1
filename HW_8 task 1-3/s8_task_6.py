# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
from pathlib import Path
import json
import pickle

__all__ = ['pickle_2_csv']


def pickle_2_csv(path: Path) -> None:
    with open(path, 'rb') as f_read:
        data = pickle.load(f_read)
    headers = list(data[0].keys())
    with open(path.stem + '.csv', 'w', encoding='UTF-8', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=headers, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    pickle_2_csv(Path('new_users.pickle'))
    