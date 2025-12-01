# Листинг 5.4
class Car:
    max_speed = 90  # Максимально допустимая скорость на дорогах
    def __init__(self, brand='Ford', weight=900, power=150, colour='Красный'):
        self.brand = brand  # Марка, модель автомобиля
        self.weight = weight  # Вес автомобиля
        self.power = power  # Мощность двигателя
        self.colour = colour  # Мощность двигателя
        self.signal = 'Би-Бип'  # Имитация звука сигнала

# Изменение общих атрибутов класса
print('Допустимая скорость в исходном классе ->', getattr(Car, 'max_speed'))
# Меняем атрибутов класса
setattr(Car, 'max_speed', 110)
print('Новая скорость в исходном классе ->', Car.max_speed)

MyCar = Car()  # Создаем объект
print('Допустимая скорость объекта ->', getattr(MyCar, 'max_speed'))
# Изменение атрибута объектов
setattr(MyCar, 'max_speed', 120)
print('Новая скорость у объекта ->', getattr(MyCar, 'max_speed'))
print('Скорость в исходном классе не изменилась->', Car.max_speed)
print('-'*30)

# Добавить атрибут классу (тормозной путь 50 м.)
setattr(Car, 'brake_dist', 50)
print('Тормозной путь -', Car.brake_dist, 'м.')

# Удаляем существующий атрибут класса
delattr(Car, 'max_speed')
print('Максимальная скорость -', hasattr(Car, 'max_speed'))