# Листинг 5.11
# 1-й супер класс
class A:
    # Устанавливаем экземпляру атрибуты
    def set_a(self):
        self.x = 111    # Обычный атрибут
        self.__y = 111  # y изменяется в _A__y.

    # Получаем атрибуты
    def get_a(self):
        print(self.x)
        print(self.__y)

# 2-й супер класс
class B:
    # Устанавливаем экземпляру атрибуты
    def set_b(self):
        self.x = 222     # Обычный атрибут
        self.__y = 222  # y изменяется в _B__y

    # Получаем атрибуты
    def get_b(self):
        print(self.x)
        print(self.__y)

# Пустой класс, наследник 2-х супер классов
class C(A, B):
    pass

# Создаем объект на основе класса C
obj = C()
print('Исходный словарь атрибутов класса "C" ')
print(obj.__dict__)
print('-'*60)

obj.set_a()  # Теперь obj.x == 1 и _A__y == 1.
print('Словарь атрибутов класса "C" после вызова метода obj.set_a()')
print(obj.__dict__)
print('-'*60)

obj.set_b()  # obj.x переопределен на 2 и _B__y == 2.
print('Словарь атрибутов класса "C" после вызова метода obj.set_b()')
print(obj.__dict__)
print('-'*60)

print('Значения атрибутов класса "C" при вызове метода obj.get_a()')
obj.get_a()
print('-'*60)

print('Значения атрибутов класса "C" при вызове метода obj.get_b()')
obj.get_b()