number = input("Enter a number, and i will tell you if it is even or odd: ")
number = int(number)

if number % 3 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")
# Оператор % не сообщает частное от целочисленного деления;он возвращает только остаток.
