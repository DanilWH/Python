from random import randint


while True:
    first = randint(1, 100)
    number = input("Я згадал число от 1 до 100, попробуй отгадать его: ")
    if number == 'выход':
    	break
    while True:
    	if number != 'выход':
    		number = int(number)
    		if number < first:
    			number = input("Слишком мало, попробуй ещё раз:")
    			if number == 'выход':
    				break
    			else:
    				continue
    		elif number > first:
    			number = input("Слишком много, давай ещё раз: ")
    			if number == 'выход':
    				break
    			else:
    				continue
    		elif number == first:
    			print("Всё верно!")
    			break


    real = input("Хотите сыграть ещё раз? ")
    if real == 'да':
    	continue
    else:
    	break
