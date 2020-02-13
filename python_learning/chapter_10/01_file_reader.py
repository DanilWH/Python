with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
# Пример программы, которая открывает файл, читает и выводит его.

# функция open() возвращает обьект, представляющий файл (в данном случае: pi_digits.txt).

# Метод read() читает всё содержимое файла и сохраняет его содержимое в одной длинной строке(в данном случае в переменной contents).

# "Чтение всего файла" стр.186-187.

print(" ")

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
# Для последовательной обработки каждой строки в файле можно возпользоваться циклом for.

# Вызов rstrip()в команде print удаляет лишние пустые строки.

# "Чтение по строкам" стр.188-189.

print(" ")

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())
# Чтобы содержимое файла оставалось доступным за пределами блока with, нужно сохранить строки файла в списке внутри блока и в далнейшем можно будет работать с полученным списком.

# Метод readlines() последовательно читает каждую строку из файла и сохраняет её в списке, а список сохраняется в переменной lines.

# "Создание списка строк по содержимому файла" стр. 189-190.

print(" ")

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))
# Пример построения одной строки со всеми цифрами из файла без промежуточных пропусков.

# "Работа с содержимым файла" стр. 190-191.

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
# Такой же код может работать с неограниченным количеством символов, например с 1 000 000 символов.

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

birthday = input("Enter your birthday, in the from mm:dd:yy: ")
if birthday in pi_string:
	print("your birthday appears in the first million digits of pi!")
else:
	print("Yor birthday does not appear in the first million dogots of pi!")
# Пример программы, которая проверяет присутствует ли день рождения в числе пи.
# "Проверка дня рождения" стр. 192-193.
