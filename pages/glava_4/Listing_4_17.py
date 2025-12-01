# Листинг 4.17
# Обычная функция с именем
def my_func(x, y, z):
    rez = x + y + z
    return rez

sum_0 = my_func(5, 10, 15)
print('Результат sum_0-> ', sum_0)

# lambda функция
# явно присваиваем его переменной
lambda_1 = lambda x, y, z: x + y + z
sum_1 = lambda_1(5, 10, 15)
print('Результат sum_1-> ', sum_1)

# Используем значения по умолчанию
lambda_2 = lambda x=8, y=4: x / y
rez_2 = lambda_2()
rez_3 = lambda_2(12)
print('rez_2 =', rez_2)
print('rez_3 =', rez_3)

# Собираем аргументы в кортеж
lambda_3 = lambda *nums: sum(nums)
sum_2 = lambda_3(2, 3)
sum_3 = lambda_3(1, 2, 3, 4, 6, 6)
print('sum_2 =', sum_2)
print('sum_3 =', sum_3)

# Используем простейшую логику
lambda_4 = lambda x, y: x / y if y != 0 else None
log_1 = lambda_4(20, 5)
log_2 = lambda_4(20, 0)
print('log_1 =', log_1)
print('log_2 =', log_2)