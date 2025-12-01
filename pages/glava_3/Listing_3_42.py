# Листинг 3.42
import os
text = 'Это первая строка текста\nЭто вторая строка текста\nЭто третья строка текста\n'
with open('my_file.txt', 'w', encoding="utf-8") as file_txt:
    file_txt.write(text)

# Получить информацию о файле
my_file = open("my_file.txt")
print(my_file)
if os.path.isfile('my_file.txt'):
    os.remove('my_file.txt')