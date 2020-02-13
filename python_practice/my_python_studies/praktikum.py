from string import ascii_letters,digits
from random import choice
message = ascii_letters + digits
number = 12
print(''.join(choice(message) for g in range(number)))
# .join обединяет элементы списка в строку, разделяя их символами введёными в пустые ковычки(например пробелы).

import collections
c = collections.Counter()
for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
    c[word] = c[word] + 1
print(c)
print(c['counter'])
print(c['collections'])
# Пример подсчёта количества повторяемых элементов в списке с использованием стандартной библиотеки Python.

A = ['red', 'green', 'blue', 5, 3, 35]
print(' '.join(map(str, A)))
# map - применяет какую-либо функцию(функции) к каждому элементу списка.

"""
Если элементы списка вводятся в одной строке, разделенные пробелами, то функция input() не поможет разделить строку на слова.

В этом случае строку можно считать функцией input(), после этого использовать метод строки split(), возвращающий список строк, разрезав исходную строку на части по пробелам. Пример:

	A = input().split()

Если при запуске этой программы ввести строку 1 2 3, то список A будет равен [‘1’, ‘2’, ‘3’]. Обратите внимание, что список будет состоять из строк, а не из чисел. Если хочется получить список именно из чисел, то можно затем элементы списка по одному преобразовать в числа:

	for i in range(len(A)):
   		A[i] = int(A[i])

Используя функции языка map и list то же самое можно сделать в одну строку:

	A = list(map(int, input().split()))
"""

filenames = ['chapter_10/limitations.txt', 'chapter_10/peter.txt',
	'chapter_10/walking_essays.txt']

for filename in filenames:
	with open(filename, encoding='utf8') as file_object:
		content = file_object.read()
		print(filename + " have " + str(content.lower().count('the')) +
			" words 'the'")
# Эта программа не работает так как текстовые файлы находятся в другом каталоге(в каталоге chapter_10).

"""
Если у текстового(.txt) файла какая либо другая кодировка, в функцию open() нужно написать encoding='utf8'. Пример:
(with open(filename, encoding='utf8') as file_object:)
"""
