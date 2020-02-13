rios = {
	'rein': 'switzerland',
	'amazon': 'south america',
	'danube': 'germany',
}

for rio, country in rios.items():
	print("the " + rio.title() +
		" The river flows through such a country as:" +
		country.title() + ".")
# Задание 1 упражнения 6-5.
for rio in rios.keys():
	print(rio.title())
# Задание 2 упражнения 6-5.

for country in rios.values():
	print(country.title())

print(' ')# Для отступа.

# Задание 3 упражнения 6-5.

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

new_peoples = ['danil', 'edward', 'galya', 'jen', 'dasha']

for people in new_peoples:
	print(people.title() + ":")

	if people in favorite_languages:
		print("Thanks for participation in survey " + people.title() + ".\n")# Спасибо за участие в опросе.
	else:
		print(people.title() + ", please take part in our survey!\n")# Пожалуйста, примите участие в нашем опросе!
# Упражнение 6-6.
