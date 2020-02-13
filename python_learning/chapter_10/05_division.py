try:
	print(5/0)
except ZeroDivisionError:
	print("You can not divide by zero!")
# Командв print(5/0), порождающая ошибку, находится в блоке try.

# Если код в блоке try выполнен успешно, то Python пропускает блок except. Если код в болке try порождает ошибку, то Python ищет блок except с соответствующей ошибкой и выпускает код в этом блоке.

# "Блоки try-except" стр.196-197.

print("Give me two numbres, and I will divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can not divide by zero!")
	else:
		print(answer)
# Правильная обработка ошибок особенно важна в том случае, если программа должна продолжить работу после возникновения ошибки.

# "Использование исключений для предотвращения аварийного завершения программы." стр. 196-197.

# Подробнее как работает этот код на стр. 197-198 "Блок else."
