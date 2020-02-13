filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.read()
	print(lines)
# Выводит техст с чтением файла.
print(" ")

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
# Выводит текст с перебором всех строк(с использованием метода strip()).

print(" ")

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
# Выводит текст с сохранением строк в списке с последующим выводом списка вне блока with.

# Упражнение 10-1.
print(" ")

filename = 'learning_python.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.replace('Python', 'PHP').rstrip())
# Упражнение 10-2.
