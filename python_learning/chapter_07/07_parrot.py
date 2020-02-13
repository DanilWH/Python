prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)
# Пока в переменную message не введётся строка 'quit', Python будет выполнять цикл while. При вводе слова 'quit' python перестаёт выполнять цикл while, а программа завершается.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	
	if message != 'quit':
		print(message)
# Программа работает не плохо, если не считать того, что она выводит слово 'quit', словно оно является обычным сообщением. Простая проверка if решает проблему.
# "Пользователь решает прервать программу" стр. 125-126.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)
# Если программа должна выполняться только при истинности нескольких условий, нужно определить одну переменную-флаг.
# Программу можно написать так, чтобы она продолжала выполнение, если флаг находится в состоянии True, и завершалась, если любое из нескольких событий перевело флаг в состояние False.
# Пока переменная active остаётся равной True, цикл выполняется.
# "Флаги" стр. 126-127.
