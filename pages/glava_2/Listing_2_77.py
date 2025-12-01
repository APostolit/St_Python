# Листинг 2.77
# Формируем кортеж
tpl = (1, 2, 3, [4, 5])
print('Исходный кортеж->', tpl)
print('-'*35)

answer = 2 in tpl
print('Число 2 есть в tpl? ->', answer)

answer = 5 in tpl
print('Число 5 есть в tpl? ->', answer)

answer = 5 in tpl[3]
print('Число 5 есть в tpl[3]? ->', answer)

answer = 2 in tpl[3]
print('Число 2 есть в tpl[3]? ->', answer)