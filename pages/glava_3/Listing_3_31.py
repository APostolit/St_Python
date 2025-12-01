# Листинг 3.31
list_1 = [1, 2, 3]  # Создаем список
print('Исходный список')
my_txt = ''
for e in list_1: my_txt += str(e) + ' '
print(my_txt)  # Выводим элементы списка
print('-'*60)

# Получаем объект-итератор из списка посредством функции iter()
obj_iter = iter(list_1)  # создаем объект-итератор
print('Исходный список в виде объекта obj_iter')
print('obj_iter: ', obj_iter)

print('Элементы obj_iter с помощью функции next(obj_iter)')
print('Элемент списка ->', next(obj_iter))
print('Элемент списка ->', next(obj_iter))
print('Элемент списка ->', next(obj_iter))
print('-'*60)

obj_iter = iter(list_1)  # создаем объект-итератор заново
print('Элементы obj_iter с помощью функции next(obj_iter, default)')
print('Элемент списка ->', next(obj_iter, '<- Список закончился ->'))
print('Элемент списка ->', next(obj_iter, '<- Список закончился ->'))
print('Элемент списка ->', next(obj_iter, '<- Список закончился ->'))
print('Элемент списка ->', next(obj_iter, '<- Список закончился ->'))
print('Элемент списка ->', next(obj_iter, '<- Список закончился ->'))
print('Элемент списка ->', next(obj_iter, '<- Список закончился ->'))