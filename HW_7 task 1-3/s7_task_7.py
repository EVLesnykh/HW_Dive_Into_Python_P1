# Задание №7
#- Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
#- Каждая группа включает файлы с несколькими расширениями.
#- В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

# Решение:

from __future__ import annotations

import os
import shutil
from pathlib import Path
from random import choices, randint
from string import ascii_lowercase, digits

__all__ = ['gen_files', 'sort_files', 'gen_different_files']

def gen_files(ext: str, min_name: int = 6, max_name: int = 30, min_size: int = 256,
              max_size: int = 4096, file_count: int = 42) -> None:
    for _ in range(file_count):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}.{ext}').is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)

def sort_files(path: str | Path, groups: dict[str:list[str]] = None) -> None:
    if not groups:
        groups = {
            Path("video"): ['avi', 'mov', 'mk4', 'mkv'],
            Path("images"): ['bmp', 'jpeg', 'jpg', 'png']
        }
    os.chdir(path)
    reverse_groups = {}
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for ext in ext_list:
            reverse_groups[f'.{ext}'] = target_dir

    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)


def gen_different_files(directory: str | Path, **kwargs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    os.chdir(directory)
    for ext, numbers in kwargs.items():
        gen_files(ext, file_count=numbers)

if __name__ == '__main__':
    gen_different_files(r'C:\Users\Андрей\Desktop\git_education\HW_Dive_Into_Python_P1\HW_7 task 1-3\different_files', avi=2,
                        doc=4, bin=3, jpg=5, mkv=6, png=3)
    sort_files(Path(r'C:\Users\Андрей\Desktop\git_education\HW_Dive_Into_Python_P1\HW_7 task 1-3\different_files'))
