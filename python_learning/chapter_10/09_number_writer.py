# Модлуь json используется для записи простых структур Python в файл и загрузку данных из файла при следующем запуске программы.

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
	json.dump(numbers, file_object)
# Функция json.dump() получает два аргумента: сохраняемые данные и объект  файла, используемый для созранения.

# "Функции json.dump() и json.load()" стр.204-205.
