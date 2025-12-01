# Листинг 2.108
# Сохраняем множества в переменных
s_1 = {"Понедельник",  "Вторник", "Среда"}
s_2 = {"Вторник", "Среда", "Четверг"}
s_3 = {"Четверг", "Пятница", "Суббота"}

print('    Исходные множества')
print('Days1 - >', s_1)
print('Days2 - >', s_2)
print('Days3 - >', s_3)

print('     Метод issubset()')
res = s_1.issubset(s_2)
print('s_1.issubset(s_2) ->', res)
print('     Метод isdisjoint()')
res = s_1.isdisjoint(s_2)
print('s_1.isdisjoint(s_2) ->', res)
res = s_1.isdisjoint(s_3)
print('s_1.isdisjoint(s_3) ->', res)

# Методы получения новых множеств
print('      Объединение: (s_1, s_2, s_3) методом union()')
res1 = set.union(s_1, s_2, s_3)
print(res1)
res2 = s_1.union(s_2, s_3)
print(res2)
print('-'*65)

print('      Пересечение (s_2, s_3) методом intersection()')
res = s_1.intersection(s_2, s_3)
print(res)
print('-'*65)

print('      Разность (s_1, s_2, s_3) методом difference()')
res = set.difference(s_1, s_2, s_3)
print('set.difference(s_1, s_2, s_3) ->', res)
print('-'*65)

print('      Разность (s_1, s_2 методом symmetric_difference()')
res = s_1.symmetric_difference(s_2)
print(res)