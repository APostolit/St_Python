# Листинг 3.36
# Импортируем модуль sys
import sys

# Генератор создает список
li_1 = [x for x in range(0, 1000000)]
print('Размер памяти, занятой списком li_1:', sys.getsizeof(li_1))

# Генератор создает множество
s_1 = {x for x in range(0, 1000000)}
print('Размер памяти, занятой множеством s_1:', sys.getsizeof(s_1))

# Генератор-выражение создает итератор
gen_1 = (x for x in range(0, 1000000))
print('Размер памяти, занятой итератором gen_1:', sys.getsizeof(gen_1))

rem_s1 = sys.getsizeof(s_1)
rem_g1 = sys.getsizeof(gen_1)
rez = rem_s1 / rem_g1
print('Сокращение объема памяти - ', rez)