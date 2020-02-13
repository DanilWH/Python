n = [5,10,20,25,35,40]
rights = 0
errors = 0
points = 0
while True:
	push = input("Стреляй!!!")

	if push == 'хватит':
		push = str(push)
		break
	elif 'хватит' not in n:# Если слово "хватит" не ввели в переменную, то...
		push = int(push)
		if errors == 9:
			print("Ты совершил 10 промахов, GAME OVER!")
			break
		elif (push <= n[1]) and (push >= n[0]):
			print('Бум, ты попал как снайпер! Первая цель поражена!')
			rights = rights + 1
			points = points + 5
		elif (push <= n[3]) and (push >= n[2]):
			print('WOW! Цель №2 уничтожена!')
			rights = rights + 1
			points = points + 5
		elif (push <= n[-1]) and (push >= n[-2]):
			print('Ух ты! вот и третья цель уничтожена!')
			rights = rights + 1
			points = points + 5
		else:
			print('Мозява!')
			errors = errors + 1
			
print("Количество твоих очков", points)
print("Количество твоих попаданий", rights)
print("Количество твоих промахов", errors)