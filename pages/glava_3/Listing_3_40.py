# Листинг 3.40
x = 0
try:
    y = 100 / x
    print('y =', y)
except ValueError:
    print("Это не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except TypeError:
    print("Неожиданная ошибка")
else:
    print("Код выполнился без ошибок")
finally:
    print("Я выполняюсь в любом случае!", 'x =', x)
    print('-'*40)

x = 'Это строка символов'
try:
    y = 100 / x
    print('y =', y)
except ValueError:
    print("Это не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except TypeError:
    print("Неожиданная ошибка")
else:
    print("Код выполнился без ошибок")
finally:
    print("Я выполняюсь в любом случае!", 'x =', x)
    print('-' * 40)

x = 10
try:
    y = 100 / x
    print('y =', y)
except ValueError:
    print("Это не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except TypeError:
    print("Неожиданная ошибка.")
else:
    print("Код выполнился без ошибок")
finally:
   print("Я выполняюсь в любом случае!", 'x =', x)