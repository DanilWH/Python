import json

filename = 'numbers.json'
with open(filename) as file_object:
	numbers = json.load(file_object)
print(numbers)
# Функция json.load() используется для загрузки информации из numbers.json; эта информация сохраняется в переменной numbers.

# Модуль json позволяет органицовать простейший обмен данными между программами.

# "Функции json.dump() и json.load()" стр.204-205.
