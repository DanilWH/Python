name = input("What is your name? ")

filename = 'guest.txt'
with open(filename, 'w') as file_object:
	file_object.write(name)
# Упражнение 10-3.

filename = 'guest_book.txt'
while True:
	"""Сохраняет приветствие в текстовом файле."""
	name = input("What is your name? ")
	if name == 'q':
		break
	else:
		message = "Hello " + name + "!"
		print(message)
		with open(filename, 'a') as file_object:
			file_object.write(message + "\n")
# Упражнение 10-4.

filename = 'question_about_programming.txt'
while True:
	"""Сохраняет ответ на вопрос в текстовом файле."""
	question = input("Why you like to program? ")
	if question == 'q':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(question + "\n")
# Упражнение 10-5.
