while True:
	factorial = input(
		'Enter a number for calculate factorial or "q" to exit: ')
	if factorial == 'q':
		break
	else:
		factorial = int(factorial)
		count = 1 # вычисление факториала начинается с одного.
		answer = 1
		while count <= factorial:
			answer *= count
			count += 1

		print(answer)