# Листинг 3.44
import os
# Запись информации в файл
text = 'Это первая строка текста\nВ этом программном модуле\nиспользуется кодировка UTF-8\n'
with open('my_file.txt', 'w', encoding="utf-8") as file_txt:
    file_txt.write(text)

# Чтение информации из файла
with open('my_file.txt', 'r', encoding="utf-8") as file_txt:
    data_text = file_txt.read()

# Получить информацию о файле
print(file_txt)
print('-'*30)

print(data_text)  # Вывести содержимое файл
print('-'*30)

# Вывести содержимое файл
for line in data_text.splitlines():
    print(line)

if os.path.isfile('my_file.txt'):
    os.remove('my_file.txt')