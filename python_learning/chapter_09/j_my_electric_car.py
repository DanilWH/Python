from g_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# В одном модуле можно хранить сколько угодно классов.
# "Хранение нескольких классов в модуле" стр. 178-179.

"""
Файл может не работать так как в g_car отсутствуют классы ElectricCar и Battery.
"""