# Листинг 3_4
print('Исходный список фруктов')
fruits = ['Лимоны', 'Апельсины', 'Мандарины', 'Яблоки']
print('Фрукты ->', fruits)
print('----- Распаковываем список фруктов -----')
f_1, f_2, *f_3 = fruits
print('f_1->', f_1)
print('f_2->', f_2)
print('f_3->', f_3)
print('Тип данных fruits->', type(fruits))
print('Тип данных f_3->', type(f_3))
print('=' * 30)

print('Исходный кортеж овощей')
vegetables = ('Огурцы', 'Помидоры', 'Капуста', 'Морковь')
print('Овощи ->', vegetables)
print('----- Распаковываем кортеж овощей -----')
ov_1, ov_2, *ov_3 = vegetables
print('ov_1->', ov_1)
print('ov_2->', ov_2)
print('ov_3->', ov_3)
print('Тип данных vegetables->', type(vegetables))
print('Тип данных ov_3->', type(ov_3))
print('=' * 30)

print('Исходные словари')
d_1 = {1: "Пн", 2: "Вт", '3': "Ср"}
d_2 = {4: "Чт", 5: "Пт", '6': "Сб", 7: "Вс"}
print('d_1 ->', d_1)
print('d_2 ->', d_2)
print('----- Объединенный словарь -----')
all_d = {**d_1, **d_2}
print(all_d)