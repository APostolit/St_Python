# Листинг 5.10
# Создаем супер класс
class A:
    def method_0():  # Метод супер класса - не будем менять
        print('-> 0000  Это method_0 в супер классе  A  <-')

    def method_1(self):  # 1-й метод супер класса
        print('-> AAAA  Это method_1 в супер классе A  <-')

    def method_2(self):  # 2-й метод супер класса
        print('-> AAAA  Это method_2 в супер классе A  <-')

# Первый подкласс - наследник супер класса A
class B(A):
    def method_1(self):  # Расширяем 1-й метод супер класса A
        # Используем метод супер класса A.
        # Можно и через super().method_1().
        super(B, self).method_1()
        # Своя функциональность
        print('-> BBBB  Это method_1 в классе B»')

# Второй подкласс - наследник супер класса B
class C(B):
    # Расширяем 2-й метод супер класса A.
    def method_2(self):
        super(B, self).method_2()  # Используем метод супер класса A
        # Своя функциональность
        print('-> CCCC Это method_2 в классе C  <-')

# Создаем объект из подкласса C
obj = C()

# Вызываем методы классов
obj.method_1()
print('-'*45)

obj.method_2()
print('-'*45)

super(B, obj).method_1()
print('-'*45)

super(B, C).method_0()