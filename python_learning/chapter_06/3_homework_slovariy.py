man_0 = {
	'first_name': 'danil',
	'last_name': 'lomakin',
	'age': 15,
	'city': 'los-angeles',
	}
man_1 = {
	'first_name': 'natasha',
	'last_name': 'lomakina',
	'age': 46,
	'city': 'zlatoust',
	}
man_2 = {
	'first_name': 'oleg',
	'last_name': 'lomakin',
	'age': 43,
	'city': 'zlatoust'
}
people = [man_0, man_1, man_2]
for info in people:
	print(info)

# Упражнение 6-7(переделанное 6-1).
print(man_0['first_name'].title())
print(man_0['last_name'].title())
print(man_0['age'])
print(man_0['city'].title())

# Упражнение 6-1.

numbers = {
	'danil': [6],
	'natasha': [7],
	'oleg': [27],
	'user_0': [64,34],
	'user_1': [43,55,94],
	}
for name, number in numbers.items():
	print(name.title() + ":")
	for number in number:
		print("\t" + str(number))
# Изменённое упражнение 6-2 на 6-10.

golossariy = {
	'concatenation': 'line break',
	'variable': 'place of memory',
	'list': 'itemset',
	'if': 'condition',
	'tuples': 'an immutable list',
	}
print("\nConcatenation:\n\t" +
	golossariy['concatenation'] +
	".\n")
print("Variable:\n\t" +
	golossariy['variable'] +
	".\n")
print("List:\n\t" +
	golossariy['list'] +
	".\n")
print("If:\n\t" +
	golossariy['if'] +
	".\n")
print("Tuples:\n\t" +
	golossariy['tuples'] +
	".\n")

# Далее будут упражнения 6-4.
print(" ")

golossariy = {
	'concatenation': 'line break',
	'variable': 'place of memory',
	'list': 'itemset',
	'if': 'condition',
	'tuples': 'an immutable list',
	}

golossariy['dictionary'] = 'the creation of real objects'
golossariy['"keys()"'] = 'if you are only interested in the keys pars'
golossariy['"value()"'] = 'if you are only interested in the values pars'
golossariy['"items()"'] = 'display vocabularies in a list'
golossariy['"sorted()"'] = 'sort lists, tuples, dictionaries, and more'

for word, definition in golossariy.items():
	print(word.title() +
		":\n\t" + definition + ".")
# Упражнение 6-4.
