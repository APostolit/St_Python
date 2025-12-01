# Листинг 5.5
# Создаем простейший класс (без методов)
class Simpl_class:
    attr_class = 0  # Атрибут класса (доступен всем экземплярам)

my_obj = Simpl_class()  # Создаем объект(экземпляр класса)
print('Начальное значение атрибута ->', my_obj.attr_class)

my_obj.attr_class = 111  # Изменяем значение атрибута у объекта
print('Измененное значение атрибута ->', my_obj.attr_class)

del my_obj.attr_class  # Удаляем атрибут из объекта (но не класса)
print("Наличие атрибута у объекта ->", hasattr(my_obj, 'attr_class'))
print('Значение атрибута объекта->', my_obj.attr_class)
print('Значение атрибута класса->', Simpl_class.attr_class)

# Здесь получим ошибку, т.к. удалять в объекте уже нечего
try:
    del my_obj.attr_class
except Exception:
    print('Ошибка удаления атрибута')