filename = 'alise.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	message = "Sorry, the file " + filename + " does not exist."
	print(message)
else:
	# Подсчёт приблизительного количества строк в файле.
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")
# Чтобы небыло трассировки при ошибочном открывании файла .txt, можно воспользоваться блоками try-except.
# "Обработка исключения FileNotFoundError" стр. 198-199.

# В блоке else выполняется подсчёт слов в текстовом файле.
# Метод split() разделяет строку на части по всем позизиям, в которых обнаружит пробел(разделяет строку на слова), и сохраняет в элементах списка.
# "Анализ текста" стр. 200-201.
