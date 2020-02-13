# Начинаем с двух списков: пользователей для проверки и пустого списка для хранения проверенных пользователей.
uncofirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# Проверяем каждого пользователя, пока остаются непроверенные пользователи. Каждый пользователь, прошедший проверку, перемещается в список проверенных.
while uncofirmed_users:
	current_users = uncofirmed_users.pop()

	print("Verifying user: " + current_users.title())
	confirmed_users.append(current_users)

# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_users in confirmed_users:
	print(confirmed_users.title())
# Пример проверки пользователей и извлечеие из списка не проверенных пользователей в список проверенных.
# Подробнее об этом на стр. 130-131.
