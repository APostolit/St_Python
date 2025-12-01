# Листинг 2.105
# Исходные множества
Days1 = {"Понедельник",  "Вторник", "Среда", "Четверг"}
Days2 = {"Пятница", "Суббота", "Воскресенье"}
Days3 = {"Вторник", "Среда"}

print('    Исходные множества')
print('Days1 - >', Days1)
print('Days2 - >', Days2)
print('Days3 - >', Days3)

print('----- Объединение множеств Days1 | Days2   ----------')
print(Days1 | Days2)
print(' ')

print('----- Пересечение множеств Days1 & Days3   ----------')
print(Days1 & Days3)
print(' ')

print('----- Разница множеств Days1 - Days3   ----------')
print(Days1 - Days3)
print(' ')

print('----- Симметричная разность двух множеств  Days1 ^ Days3   ----------')
print(Days1 ^ Days3)