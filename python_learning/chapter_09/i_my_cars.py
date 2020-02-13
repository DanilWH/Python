from g_car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# Чтобы импортировать несколько классов из модуля, нужно разделить из имена запятыми.
# "Импортирование нескольких классов из модуля" стр. 179-180.

print(" ")

import g_car

my_beetle = g_car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = g_car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# Также возможно импортировать весь модуль, а потом обращаться к нужным классам с использованием точечной записи.
# "Импортирование всего модуля" стр. 180.
print(" ")

from g_car import *

my_beetle = g_car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = g_car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# Для импортирования всех классов из модуля используется синтаксис следующего вида: from имя_модуля import *.
# Такой способ не рекомендуется использовать.
# "Импортирование всез классов из модуля." стр. 180.

"""
Файл может не работать,
так как в g_car отсутствуют классы ElectricCar и Battery.
"""
print(" ")

from g_car import Car
from k_electric_car_import import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
