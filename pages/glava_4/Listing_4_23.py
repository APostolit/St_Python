# Листинг 4.23
# Объявляем аннотированную функцию
def my_func(cena: 'Цена - руб', nalog: 'Налог -%' = 20) -> float:
    nds = cena * nalog / (100 + nalog)
    tovar = cena - nds
    return tovar, nds

print('      Получаем сведения о параметрах функции')
print(my_func.__annotations__)
print('-'*60)

cena = 200  # цена товара с НДС
print('Цена товара с НДС - ', cena)
print('-'*30)

print('     Расчет при ставке НДС 20%')
tovar, nds = my_func(cena)
itogo = round(tovar, 2) + round(nds, 2)
print('Стоимость товара - ', round(tovar, 2))
print('НДС от стоимость товара - ', round(nds, 2))
print('Итого - ', itogo)
print('-'*30)

print('     Расчет при ставке НДС 10%')
tovar, nds = my_func(cena, 10)
itogo = round(tovar, 2) + round(nds, 2)
print('Стоимость товара - ', round(tovar, 2))
print('НДС от стоимость товара - ', round(nds, 2))
print('Итого - ', itogo)