# Листинг 3.35
# Выражение-генератор без условия
gen_1 = (x ** 2 for x in range(2, 6))
print('Это объект-генератор (gen_1)')
print(gen_1)

print('Это значения, выдаваемые генератором gen_1')
txt = []
for elem in gen_1:
    txt.append(elem)
print(txt)
print('-' * 30)

# Выражение-генератор с условием if
gen_2 = (x * 10 for x in range(2, 10) if x > 4)
print('Это объект-генератор (gen_2)')
print(gen_2)

print('Это значения, выдаваемые генератором gen_2')
txt = []
for elem in gen_2:
    txt.append(elem)
print(txt)