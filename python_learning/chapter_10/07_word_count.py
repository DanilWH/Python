def count_words(filename):
	"""Подсчёт приблизителоного количества строк в файле"""
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
		print("The file " + filename + " has about " + str(num_words) + 
			" words.")

filenames = ['alise.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_woman.txt']
for filename in filenames:
	count_words(filename)
# Чтобы работать сразу с несколькоми файломи нужно основной код переместить в функцию, затем файлы, которые нужно открыть, нужно перечислить в списке как элементы и в цикле перебрать файлы для подсчёта слов.

# Файла siddhartha.txt специально не имеется для того чтобы проверить, что программа с обработкой исключений работает правильно.

# "Работа с несколькими файлами" стр. 201-202.

print(" ")

def count_words(filename):
	"""Подсчёт приблизителоного количества строк в файле"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		# Подсчёт приблизительного количества строк в файле.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + 
			" words.")

filenames = ['alise.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_woman.txt']
for filename in filenames:
	count_words(filename)
# Если нужно, чтобы при обнаружении исключения программа просто игнорировала сбой, будто ничего и небыло, нужно в блок except вписать команды pass.
# Команда pass не выдаёт данные трассировки и вообще никакие результаты, указывающие на возникновении ошибки.
# "Ошибки без уведомления" стр. 202.
