users = ['danil', 'galya', 'admin', 'dasha', 'anya']

for user in users:
	if user == 'admin':
		print("Hello " + user.title() + ", would you like to see a status report?")
	else:
		print("Hello " + user.title() + ", thank you for loggin in again.")
# Упражнение 5-8.
print(' ')

users = []

if users:
	for user in users:
		if user == 'admin':
			print("Hello " + user.title() + ", would you like to see a status report?")
		else:
			print("Hello " + user.title() + ", thank you for loggin in again.")
else:
	print("We need to find some users!")
# Упражнение 5-9.

print(' ')

current_users = ['Galya', 'DAnil', 'Asha', 'Anya', 'Aydar']
current_users = [users.lower() for users in current_users]# В новую переменную users присваивается новый список с нижним регистром для всех элементов из списка current_users.
new_users = ['vova', 'galya', 'kiril', 'danil', 'misha']

if new_users:# Если в списке new_users что-то имеется, то происходит следующее.
	for users in new_users:# Для переменной users перезамисывается новый список из new_users.
		if users.lower() in current_users:# Для этого списка users(то есть, по идее для new_users.), применяется нижний регистр, а за тем if проверяет, имеется ли в списке новых пользователей(в списке users или по другому new_users), что схоже в списке старых пользоветелей(в списке current_users). Если имеется то происходит следующее.
			print("Name " + users.title() + " already in use.")
		else:# Если элементов, схожих со списком старых пользователей не имеется, происходит следуещее.
			print(users.title() + ", you are registered.")
# Упражнение 5-10.
print(' ')

number = [1,2,3,4,5,6,7,8,9]
for number in number:
	if number == 1:
		print(str(number) + 'st')
	elif number == 2:
		print(str(number) + 'nd')
	elif number == 3:
		print(str(number) + 'rd')
	else:
		print(str(number) + 'th')
# Упражнение 5-11.
