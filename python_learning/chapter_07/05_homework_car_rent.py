car = input("What car will you drive? ")
print("Let's me see if i can find you a " + car.title() + ".")
# Упражнение 7-1.

table = input("How many seats do you want to book a table for? ")
table = int(table)

if table > 8:
	print("You'll have to wait!")
else:
	print("Your table is ready!")
# Упражнение 7-2.

number = input("Input number: ")
number = int(number)

if number % 10 == 0:
	print("Number " + str(number) + "even.")
else:
	print("Number " + str(number) + " odd.")
# Упражнение 7-3.
