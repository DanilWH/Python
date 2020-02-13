user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

for key, value in user_0.items():
	print("Key:" + key.title())
	print("Value:" + value.title() + "\n")
# В цикле ставим две переменных. Первая для хранения ключа пары, вторая для хранение значения пары.
# items() возвращает список пар "ключ-значение", без него будет ошибка(я так понимаю).
# Подробнее на стр.108-109 "Перебор всех пар ключ-значение".

# Продолжение в 2_favorite_languages.py

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
		language.title() + ".")
# Второй пример перебора словарей.

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in favorite_languages.keys():
	print(name.title())
	# Код будет работать так же если метода keys() не было, но лучше использовать этот метод так как он  упрощает чтение кода.
# Метод keys() удобен в тех случаях когда не нужно работать со всеми значениями в словаре.

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")
# 								 ^ Чтобы получить язык в этой точке, нужно использовать имя словаря и текущее значение name как ключ.

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll\n")
# Метод keys() также может использоваться для проверки того, учавствовал ли конкретный человек в опросе.
# Метод keys() не ограничивается перебором: он возвращает список всех ключей.
# Подробнее на стр.110-111.

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
# sorted(favorite_languages.keys()) эта конструкция приказывает Python выдать список всех ключей в словаре и отсортировать его перед тем как перебирать элементы.

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("\nThe following languages have been mentioned:")# будут упомянуты следующие языки:
for language in favorite_languages.values():
	print(language.title())
# Если прежде всего интересны значения, содержащиеся в словаре, нужно использовать метод values()

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
# Чтобы получить список выбранных языков без повторений, можно возпользоваться множеством (set). (set)используется для извлечения уникальных языков из favorite_languages.values(). В результате создаётся список не сожержащий дубликатов.

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
user_1 = {
	'username': 'daniel',
	'first': 'danil',
	'last': 'lomakin',
	}
user_2 = {
	'username': 'galiyaamazing',
	'first': 'galya',
	'last': 'pleshakova',
	}

users = [user_0, user_1, user_2]

for user in users:
	print(user)
# Пример со списком в словаре со стр.115-116 "вложение".
