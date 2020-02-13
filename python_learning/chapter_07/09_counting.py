current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)
# Вместо того чтобы полностю прерывать выполнение цикла без выполнения оставшеёся части кода, можно воспользоватся командой continue.
# Команда continue приказывает Python проигнорировать оставшийся код цикла и вернутья к началу цикла.

x = 1
while x <= 5:
	print(x)
	x += 1
# Если пропустить строку x += 1, то создастся безконечный цикл.
