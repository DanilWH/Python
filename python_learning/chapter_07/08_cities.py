prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
# Команда break прерывает цикл while без выполнения оставшегося кода в цикле независимо от состояния условия, используйте команду break.
