while True:
	try:
		first_number = input("Enter first number: ")
		if first_number == 'q':
			break
		first_number = int(first_number)

		last_number = input("Enter last number: ")
		if last_number == 'q':
			break
		last_number = int(last_number)

		answer = int(first_number) + int(last_number)
	except ValueError:
		print("Incorrect input!")
	else:
		print(answer)
# Упражнение 10-6 и 10-7.

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	try:
		with open(filename) as file_object:
			contents = file_object.read()
			print(contents)
	except FileNotFoundError:
		print("File " + filename + " not available.")
# Упражнение 10-8.

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	try:
		with open(filename) as file_object:
			contents = file_object.read()
			print(contents)
	except FileNotFoundError:
		pass
# Упражнение 10-9.

filenames = ['limitations.txt', 'peter.txt', 'walking_essays.txt']

for filename in filenames:
	with open(filename, encoding='utf8') as file_object:
		content = file_object.read()
		print(filename + " have " + str(content.lower().count('the')) +
			" words 'the'")
# Упражнение 10-10.
"""
Если у текстового файла какая либо другая кодировка, в функцию open() нужно написать encoding='utf8'. Пример:
(with open(filename, encoding='utf8') as file_object:)
"""
