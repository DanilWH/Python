# Задача с аттракционами.
age = 12
if age < 4:
	print('Your admission cost is $0.')
elif age <18:
	print('Your admission cost is $5.')
else:
	print('Your admission cost is $10.')
# Строка elif в действительности является ещё одной проверкой if. Подробнее об этом на странице 91-92 под заголовком "Цепочки if-elif-else".

age = 12 
if age < 4:
	prise = 0
elif age < 18:
	prise = 5
else:
	prise = 10
print('Your admission cost is $' + str(prise) + '.')
# Лучше использавать компактное решение как это. Так оно более правильнее, читаемое и имеет более чёткую специализацию.
# Кроме повышение эффективности, у этого кода есть дополнительное преимущество: лучшая изменяемость. Чтобы изменить текст выходного сообщения, достаточно будет отредактировать всего одну команду print-вместо трёх разных команд.

# Пример с особой скидкой для пожилых посетителей.
age = 12 
if age < 4:
	prise = 0
elif age < 18:
	prise = 5
elif age < 65:
	prise = 10
else:
	prise = 5
print('Your admission cost is $' + str(prise) + '.')

# Отсутстиве блока else.
age = 12
if age < 4:
	prise = 0
elif age < 18:
	prise = 5
elif age < 65:
	prise = 10
elif age >= 65:
	prise = 5
print('Your admission cost is $' + str(prise) + '.')
# Python не требуеть чтобы цепочка if-elif непременно завершалась блоком else. В других случаях бывает нагляднее использовать дополнительную секцию elif для обработки конкретного условия.
# Если имеется завершающее конкретное условие, лучше восползоваться завершающим блоком elif и опустить(пропустить) блок else. В этом лучае можно быть уверенным в том, что код будет выполняться только в правильных условиях.