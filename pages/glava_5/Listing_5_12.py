# Листинг 5.12
class Person:
    def __init__(self):
        self.open_atr = 'Демонстрации инкапсуляции'  # Открытый атрибут
        self.__name = None  # Имя (закрытый атрибут)
        self.__age = None   # Возраст (закрытый атрибут)
    # Метод - установить (принять) имя
    def set_name(self, name):
        self.__name = name
    # Метод - установить (принять) возраст
    def set_age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")
    # Метод - получить (отдать) возраст
    def get_age(self):
        return self.__age
    # Метод - получить (отдать) имя
    def get_name(self):
        return self.__name
    # Метод - получить (отдать) информацию о персоне
    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")

my_per = Person()
print('Информация о человеке при инициализации класса')
my_per.display_info()
print('-'*25)

my_per.set_name('Иванов Иван Иванович')  # Передаем в класс имя
print('Информация о человеке после передачи в класс имени')
my_per.display_info()
print('-'*25)

print('Попытка передать в класс ошибочного возраста')
my_per.set_age(-3486)  # Передаем в класс недопустимый возраст
print('-'*25)

my_per.set_age(25)  # Передаем в класс возраст
print('Информация о человеке после передачи в класс возраста')
my_per.display_info()
print('-'*25)

print('Получить отдельно: имя, возраст')
print(my_per.get_name())
print(my_per.get_age())
print('-'*25)

print('Вывод открытых атрибутов класса')
print(my_per.open_atr)

print('Вывод закрытых атрибутов класса')
try:
    print(my_per.__name)  # Выдаст ошибку - закрытый атрибут
except Exception:
    print('Ошибка: попытка вывести закрытый атрибут')
try:
    print(my_per.__age)   # Выдаст ошибку - закрытый атрибут
except Exception:
    print('Ошибка: попытка вывести закрытый атрибут')

print('='*50)

print('Но все же возможен вывод закрытых атрибутов класса')
print(my_per._Person__name)
print(my_per._Person__age)