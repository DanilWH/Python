filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.")
"""
Второй аргумент в функции open() сообщает что должен делать Python:
'r'- открывает файл в режиме чтения. 
'w'- открывает файл в режиме записи.
'a'- открывает файлв режиме присоеденения.
'r+'- открывает файл в режиме, допускающем как чтение, так и запись в файл.
Если аргумент режима не указан, Python по умолчанию открывает файл в режиме только для чтения.
"""
# Метод write() используется с объектом файла для записи строки в файл.

# Открывая файл в режиме записи ('w'): если файл существует, Python уничтожит его данные перед возвращением объекта файла.

# "Запись в пустой файл" стр. 193-194.

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")
# Функция write() не добавляет символы новой строки в записываемый текст.
# Чтобы строки были отдельными, нужно включить символы новой строки в запись.

filename = 'programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
# Чтобы добавить в файл новые данные вместо того, чтобы перезаписывать существующее содержимое, нужно открыть файл в режиме присоеденения.

# "Присоеденение данных к файлу" стр. 194-195.
