# Листинг 3.43
import os

text = 'Это первая строка текста\nЭто вторая строка текста\nЭто третья строка текста\n'
with open('my_file.txt', 'w', encoding="utf-8") as file_txt:
    file_txt.write(text)

with open('my_file.txt', 'r') as file_txt:
    data_text = file_txt.read()

# Получить информацию о файле
print(file_txt)
print('-'*65)

# Вывести содержимое файл построчно
for line in data_text.splitlines():
    print(line)

if os.path.isfile('my_file.txt'):
    os.remove('my_file.txt')