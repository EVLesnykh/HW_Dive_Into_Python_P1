#Задание №6
#- Дорабатываем функции из предыдущих задач.
#- Генерируйте файлы в указанную директорию — отдельный параметр функции.
#- Отсутствие/наличие директории не должно вызывать ошибок в работе функции
#(добавьте проверки).
#- Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from s7_task_5 import gen_files
from pathlib import Path
import os

def create_dir(name_dir: str):
    name = Path(Path.cwd() / name_dir)
    if not name.exists():       
        name.mkdir()           

    os.chdir(name)         


if __name__ == '__main__':
    my_dict = {'.txt': 1, '.doc': 1, '.bin': 1, '.pdf': 1}
    gen_files(my_dict)
    create_dir('new')
    