# Листинг 3.37
# Создаем список при помощи функции list()
list_1 = list(x for x in range(10))
print('Список list_1:', list_1)

# Создаем кортеж при помощи функции tuple()
tup_1 = tuple(x for x in range(10))
print('Кортеж tup_1:', tup_1)

# Создаем множество при помощи функции set()
set_1 = set((x for x in range(10)))
print('Множество s_1:', set_1)