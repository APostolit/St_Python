# Листинг 3.32
li = [1, 2, 3]  # Создаем список
txt = []
for e in li: txt.append(e)
print(txt) # Получаем элементы списка в авто режиме
print('-----------')

# Используем протокол итераций и
# получаем элементы списка в ручном режиме
li_iter = iter(li)
print(next(li_iter))
print(next(li_iter))
print(next(li_iter))
print(next(li_iter, 'Конец списка'))