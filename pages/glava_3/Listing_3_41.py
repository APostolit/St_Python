# Листинг 3.41
import os
text = 'Это первая строка текста\nЭто вторая строка текста\nЭто третья строка текста\n'
file_txt = open('my_file.txt', 'w')
file_txt.write(text)
file_txt.close()

# Получить информацию о файле
my_file = open("my_file.txt")
print(my_file)

if os.path.isfile('my_file.txt'):
    os.remove('my_file.txt')