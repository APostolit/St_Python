# Листинг 3.48
# Пример использования класса Path модуля pathlib
from pathlib import Path

print('Получаем путь к домашней директории')
home_dir = Path.home()
print(home_dir)
print('-'*30)

print('Получаем путь к рабочей директории')
script_dir = Path.cwd()
print(script_dir)
print('-'*30)

print('Получаем родительскую папку рабочей директории')
parent_dir = script_dir.parent
print(parent_dir)
print('-'*30)

print('Получаем родительскую папку родителя рабочей директории')
parent_dir = script_dir.parent.parent
print(parent_dir)
print('-'*30)

print('Получаем путь к файлу из рабочей директории')
file_path_1 = Path("files", "info", "docs.txt")
print(file_path_1)
print('-'*30)

print('Получаем полный путь к файлу')
file_path_2 = Path(script_dir, 'files', 'info', 'docs.txt')
print(file_path_2)
print('-'*30)

print('Получаем тип объекта path')
print('Исходный объект path->', type(file_path_2))
file_path_2 = str(file_path_2)
print('Строковый объект path->', type(file_path_2))