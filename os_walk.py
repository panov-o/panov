import os
import time

directory = '/home/panov/UrbanUniversity/ProjectPanov1/4 модуль'

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root, file)
    filetime = os.path.getatime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Результат:

# /home/panov/PycharmProjects/PythonProject/.venv/bin/python /home/panov/PycharmProjects/PythonProject/os_walk.py
# Обнаружен файл: 04_practice.py, Путь: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль/04_practice.py, Размер: 2516 байт, Время изменения: 04.12.2024 14:00, Родительская директория: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль
# Обнаружен файл: nim_engine.py, Путь: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль/nim_engine.py, Размер: 754 байт, Время изменения: 04.12.2024 14:00, Родительская директория: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль
# Обнаружен файл: module2.py, Путь: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль/module2.py, Размер: 205 байт, Время изменения: 04.12.2024 14:00, Родительская директория: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль
# Обнаружен файл: module1.py, Путь: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль/module1.py, Размер: 90 байт, Время изменения: 04.12.2024 14:00, Родительская директория: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль
# Обнаружен файл: namespaces.py, Путь: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль/namespaces.py, Размер: 133 байт, Время изменения: 04.12.2024 14:00, Родительская директория: /home/panov/UrbanUniversity/ProjectPanov1/4 модуль
#
# Process finished with exit code 0