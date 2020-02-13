favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("Sarah's favorite language is " + 
	favorite_languages['sarah'].title() + ".")
# Чтобы узнать, какой язык выбран пользователем с именем Sarah, мы запрашиваем значение favorite_languages['sarah'].

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print("\n" + name.title() + "'s favorite language are:")
		for language in languages:
			print("\t" + language.title())
	else:
		print("\n" + name.title() + "'s favorite languages are:")
		for language in languages:
			print("\t" + language.title())
# Пример исползование списка в словаре.
# В цикле for создается другой цикл для перебора списка языков, связанных с каждым участником.
