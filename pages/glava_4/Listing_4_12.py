# Листинг 4.12
def func(x, *y, **z):
    print("Тип данных x ->", type(x))
    print('x->', x)
    print("Тип данных y ->", type(y))
    print('y->', y)
    print("Тип данных z ->", type(z))
    print('z->', z)
    return

func(111, 222, 333, y=1, a=2, b=3)