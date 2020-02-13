countries = ["америка", "япония", "китай", "норвегия", "швеция"]
print(countries)

print("Wich sorted!")
print(sorted(countries))
# Есть "временная" сортировка по алфавитному порядку.
print("Not sorted.")
print(countries)
# Нет сортировки.
print("Обратный порядок.")
print(sorted(countries, reverse=True))
#Есть "временная" сортировка по обратному алфавитному порядку.
print("Not sorted")
print(countries)
# Нет сортировки.
print("Перевёрнутый список.")
countries.reverse()
print(countries)
# Перевёрнутый список "задом на перёд".
print("Исходный список.")
countries.reverse()
print(countries)
# Исходный список элементов вернувшийся повторным применением метода reverse().
print("Wich sorted.")
countries.sort()
print(countries)
# Есть "постоянная" сортировка
print("Wich sorted(back up).")
countries.sort(reverse=True)
print(countries)
# Есть "постоянная" сортировка в обратном алфавитном порядке.
