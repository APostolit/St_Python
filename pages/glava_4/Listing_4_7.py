# Листинг 4.7
print('Функция с фиксированным количеством параметров - def my_fun_1(x, y):')
def my_fun_1(x, y):
    print('Тип переменной y ->', type(y))
    rez = x + y
    return rez

rez_1 = my_fun_1(1, 2)
print('Результат my_fun_1(1, 2) ->', rez_1)

print('Функция с одним из параметров переменной длины - def my_fun_1(x, *y):')
def my_fun_2(x, *y):
    print('Тип переменной y ->', type(y))
    rez = x + sum(y)
    return rez

rez_2 = my_fun_2(1, 2, 3)
print('Результат my_fun_2(1, 2, 3) ->', rez_2)

print('Функция с параметром переменной длины - my_fun_3(*args):')
def my_fun_3(*args):
    rez = sum(args)
    return rez

print('Результат my_fun_3() ->', my_fun_3())
print('Результат my_fun_3(1) ->', my_fun_3(1))
print('Результат my_fun_3(1, 2) ->', my_fun_3(1, 2))
print('Результат my_fun_3(1, 2, 3) ->', my_fun_3(1, 2, 3))
print('Результат my_fun_3(1, 2, 3, 4) ->', my_fun_3(1, 2, 3, 4))