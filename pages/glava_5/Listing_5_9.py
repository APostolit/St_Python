# Листинг 5.9
# Создаем супер класс
class A:
    def method_0():  # Метод супер класса - не будем менять
        print('-> 0000  Это method_0 в супер классе  A  <-')

    def method_1(self):  # 1-й метод супер класса
        print('-> AAAA  Это method_1 в супер классе A  <-')

    def method_2(self):  # 2-й метод супер класса
        print('-> AAAA  Это method_2 в супер классе A  <-')

# Подкласс - наследник супер класса A
class B(A):
    def method_1(self):  # Расширяем 1-й метод супер класса A
        # Своя функциональность
        print('-> BBBB  Это собственный method_1 в классе B»')
        super().method_2()  # Используем method_2 супер класса A (вариант 1)
        super(B, self).method_2()  # Используем method_2 супер класса A (вариант 2)

# Создаем объект из подкласса B
obj = B()

# Вызываем методы классов
obj.method_1()  # Сработает method_1 класса B
print('-'*45)

obj.method_2()  # Сработает method_2 класса A
print('-'*45)

super(B, obj).method_1()  # Сработает method_1 класса A
print('-'*45)

A.method_0()  # Сработает method_0 класса A