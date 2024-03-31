# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import json
from pathlib import Path
import csv

__all__ = ['csv_to_json']


def csv_to_json(from_path: Path, to_path: Path) -> None:
    result = []
    with open(from_path, 'r', encoding='UTF-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, row in enumerate(csv_read):
            if i != 0:
                level, id, name = row
                data = {
                    "level": int(level),
                    "id": f'{int(id):010}',
                    "name": name.title(),
                    "hash": hash(f'{name.title()}{int(id):010} ')
                }
                result.append(data)
    with open(to_path, 'w', encoding='UTF-8') as f_write:
        json.dump(result, f_write, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('new_users.json'))
    