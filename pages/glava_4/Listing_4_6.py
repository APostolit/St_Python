# Листинг 4.6
print('Функция с одним позиционными параметром def func(x, y=1):')
def func(x, y=1):
    rez = x / y
    return rez

print('-'*60)
print('Вызов функции с разными вариантами передачи аргументов')
print('func(8, 2) Результат ->', func(8, 2))
print('func(x=8, y=2) Результат ->', func(x=8, y=2))
print('func(8, y=2) Результат ->', func(8, y=2))
print('func(2) Результат ->', func(2))
print('func(x=2) Результат ->', func(x=2))