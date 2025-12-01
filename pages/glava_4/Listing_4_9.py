# Листинг 4.9
print('Функция с параметром кортеж в середине списка параметров def func(x, *y, z):')
def func(x, *y, z):
    rez = x + sum(y) + z
    return rez

print('-'*60)
print('Вызов функции с разными вариантами передачи аргументов')
print('func(5, 7, 8, z=3) Результат ->', func(5, 7, 8, z=3))
print('func(5, 6, 7, 8, 9, z=3) Результат ->', func(5, 6, 7, 8, 9, z=3))
print('func(5, z=3) Результат ->', func(5, z=3))

def func_1(x, *, z):
    rez = x + sum(y) + z
    return rez

print('func(5, 6, 7, 8, 9, z=3) Результат ->', func(5, 6, 7, 8, 9, z=3))
print('func(5, z=3) Результат ->', func(5, z=3))