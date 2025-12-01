# Листинг 4.15
Glob_var = 0.001
print('     Начало работы основного модуля')
print('Значение Glob_var в начале модуля: Glob_var =', Glob_var)
print('-'*50)

def func_1():  # Объявляем внешнюю функцию
    # Начало тела внешней функции
    print('     Начало работы функции func_1()')
    # Glob_var = 100  # Так нельзя- получим ошибку

    global Glob_var  # Даем возможность менять Glob_var в func_1 и func_2
    # Теперь можно изменять значение Glob_var
    # в функциях func_1 и func_2
    Glob_var = 100
    print('Значение Glob_var в func_1: Glob_var =', Glob_var)
    Loc_var = 11111  # Создаем локальную переменную в func_1
    print('Значение в func_1: Loc_var=', Loc_var)

    def func_2():  # Объявляем вложенную функцию
        # Тело вложенной функции
        print('     Начало работы функции func_2()')
        Glob_var = 200
        print('Значение Glob_var в func_2: Glob_var =', Glob_var)

        # Loc_var = 222  # Так нельзя- получим ошибку
        nonlocal Loc_var  # Даем возможность менять Loc_var в func_2
        Loc_var = 22222   # Изменяем значение loc_var
        print('Значение Loc_var в func_2: Loc_var =', Loc_var)
        print('-' * 50)
        return

    # Продолжение тела внешней функции
    func_2()  # Вызываем вложенную функцию func_2
    print('     Продолжение работы функции func_1()')
    print('Значение Glob_var по выходу из func_2: Glob_var =', Glob_var)
    print('Значение Loc_var по выходу func_2: Loc_var =', Loc_var)
    print('-' * 50)
    return

func_1()  # Вызываем внешнюю функцию
print('     Завершение работы основного модуля ')
print('Значение Glob_var в конце модуля: Glob_var =', Glob_var)