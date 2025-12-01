# Листинг 3.22
# Выводим символы в строки
name = 'Привет'
txt = ''
for s in name: txt = txt + s
print(txt)
print('-'*20)

name = 'ПPрyиtвoеnт'
txt = ''
# Используем функцию range(a, b, step).
for n in range(0, len(name), 2):
    # Выводим буквы через одну, начиная с первой
    txt = txt + name[n]
print(txt)
print('-'*20)

txt = ''
for n in range(1, len(name), 2):
    # Выводим буквы через одну, начиная со второй
    txt = txt + name[n]
print(txt)
print('-'*20)

# Выводим ключи и значения словаря
d = {'Один': 1, 'Два': 2}
for key in d: print(key, '->', d[key])
print('-'*20)

# Перебираем список и находим суммы элементов кортежей
sum_1 = []
d = [(1, 2), (3, 4), (5, 6)]
for x, y in d: sum_1.append(x + y)
print(sum_1)