animals = 'bear'
print(animals == 'hare')# 'Заяц' False
print(animals == 'bear')# 'Медведь' True

print(' ')

print(animals != 'snake')# 'Змея' True
print(animals != 'bear')# False
# Первое задание упражнения 5-2.
print(' ')

firm = 'Gucci'
print(firm == 'Gucci')# True
print(firm == 'gucci')# False
print(firm.lower() == 'gucci')# True
print(firm)# Gucci
# Второе задание упражнения 5-2.
print(' ')

number_0 = 25
number_1 = 6
print(number_0 > number_1)# True
print(number_0 < number_1)# False

print(number_1 < 35)# True
print(number_0 > 55)# False

print(number_0 >= 25)# True
print(number_1 >= 7)# False

print(number_1 <= 56)# True
print(number_1 <= 6)# True
print(number_0 <= 6)# False
# Третье задание упражнения 5-2.
print(' ')

word = 'beach'
obgect = 'cube'
print((word == 'beach') and (obgect == 'cube'))# True
print((word == 'game') and (obgect == 'cube'))# False
print((word == 'nice') and (obgect == 'comuter'))# False
# Применение and.
print(' ')

print((word == 'beach') or (obgect == 'cube'))# True
print((word == 'ball') or (obgect == 'cube'))# True
print((word == 'great') or (obgect == 'mouse'))# False
# Применение or.
print(' ')

list_banned_0 = ['happy', 'success', 'son', 'buttle', 'water']
print('son' in list_banned_0)# True
print('apartment' in list_banned_0)# False
# Проверка вхождения элемента в список.
print(' ')

list_banned_1 = ['danil', 'galya', 'dasha', 'anya', 'alesya']
print('karina' not in list_banned_1)# True
print('galya' not in list_banned_1)# False
# Проверка отсутствия элемента в списке.
print(' ')

list_banned_1 = ['danil', 'galya', 'dasha', 'anya', 'alesya']
name_0 = 'karina'
print(name_0 not in list_banned_1)# True
print(list_banned_1[1] not in list_banned_1)# False
# Так же, эту же операцию можно проделать с переменной
