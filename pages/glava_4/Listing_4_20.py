# Листинг 4.20
# Рекурсивная функция
def sum_n(n):
    print('n = ', n)
    if n == 0:
        return n
    else:
        return n + sum_n(n - 1)

print('Сумма чисел от 0 до 4 ->', sum_n(4))