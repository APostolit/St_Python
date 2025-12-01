# Листинг 4.5
print('Функция с тремя позиционными параметрами def func(x, y, z):')
def func(x, y, z):
    rez = x + y - z
    return rez

print('-'*60)
print('Вызов функции с разными вариантами позиционирования аргументов')
print('func(8, 2, 5) Результат ->', func(8, 2, 5))
print('func(x=8, y=2, z=5) Результат ->', func(x=8, y=2, z=5))
print('func(y=2, x=8, z=5) Результат ->', func(y=2, x=8, z=5))
print('func(z=5, x=8, y=2) Результат ->', func(z=5, x=8, y=2))
print('func(8, y=2, z=5) Результат ->', func(8, y=2, z=5))
print('func(8, z=5, y=2) Результат ->', func(8, z=5, y=2))
print('func(8, 2, z=5) Результат ->', func(8, 2, z=5))