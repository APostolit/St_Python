# Листинг 2.109
# Сохраняем множества в переменных
s_1 = {1, 2}
s_2 = {2, 3}
s_3 = {3, 4}

print('    Исходные множества')
print('s_1 - >', s_1)
print('s_2 - >', s_2)
print('s_3 - >', s_3)
print('-'*30)

# Здесь изменяется множество s_1
s_1.update(s_2, s_3)
print('Итог: s_1.update(s_2, s_3) ->', s_1)
print('-'*30)

s_1.intersection_update(s_2, s_3)
print('Итог: s_1.intersection_update(s_2, s_3) ->', s_1)
print('-'*30)

s_1.difference_update(s_2, s_3)
print('Итог: s_1.difference(s_2, s_3) ->', s_1)
print('-'*30)

s_1.symmetric_difference_update(s_2)
print('Итог: s_1.symmetric_difference_update(s_2) ->', s_1)