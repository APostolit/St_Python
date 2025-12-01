# Листинг 4.18
print('lambda-функция с одним аргументом')
f1 = lambda x: x * x + x**3 - x / 2
rez = (22 + f1(2)) / 2 + f1(3) - f1(4)
print('rez =', rez)
print('-'*15)

print('lambda-функция с двумя аргументами')
f2 = lambda x, y: x ** y - x + (x * y) / 2 + y / x
print('f2 =', f2(5, 3))
print('f2 =', f2(8, 2))
print('-'*15)

print('Список из двух lambda-функций')
list_2 = [lambda x: x**2, lambda x: x**3]
print('list_2 =', list_2[0](3))
print('list_2 =', list_2[1](3))
print('-'*15)

print('И lambda-функция, и ее аргументы внутри выражения')
rez_1 = 5 + (lambda x, y: x**y)(5, 2) - 15
print('rez_1 =', rez_1)
print('-'*15)

print('lambda-выражение c вложенным lambda-выражением')
rez_2 = (lambda x: 7 + (lambda a, b: a**b)(x, 2))(5)
print(rez_2)