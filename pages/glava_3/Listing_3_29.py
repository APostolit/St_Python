# Листинг 3.29
print('----- Создаем список "x" из строк -----')
x = ["apple", "banana", "cherry"]
print('Список "x":  ', x)
print('*'*60)

print('----- Создаем объект-итератор "x" из списка строк -----')
x = iter(["apple", "banana", "cherry"])
print('Объект-итератор "x":  ', x)
print('*'*60)

print('----- Вывод элементов итератора функцией next(x) ----- ')
print(next(x))
print(next(x))
print(next(x))
print('*'*60)

print('----- Создаем объект-итератор - "x" из списка чисел -----')
x = iter([1, 2, 3])
print('Объект-итератор "x":  ', x)
print('*'*60)
print('----- Вывод элементов итератора методом __next__() -----')
print(x.__next__())
print(x.__next__())
print(x.__next__())