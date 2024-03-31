# Задание №3 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import csv
import json
from pathlib import Path

__all__ = ['json_to_csv']


def json_to_csv(path: Path) -> None:
    with open(path, 'r', encoding='UTF-8') as f_read:
        data = json.load(f_read)

    result = []
    for level, id_name in data.items():
        for id, name in id_name.items():
            result.append({'level': int(level), 'id': int(id), 'name': name})
    with open(path.stem + '.csv', 'w', encoding='UTF-8', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(result)


if __name__ == '__main__':
    json_to_csv(Path('users.json'))
    