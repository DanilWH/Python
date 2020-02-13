dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# Кортеж-список элементов, который не может изменяться.

dimensions = (200,50)
# dimensions[1] = 70
print(dimensions[0])
print(dimensions[1])
# Как видим, в этом примере изменение элемента кортежа невозвожно.

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
# Для перебора всех значений в кортеже используется цикл for, как и при работе со списками.

dimensions = (200,50)
print('\nOriginal dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,200)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)
# Чтобы заменит значения картежа, нужно переопределить весь кортеж, как показано в примере выше.
