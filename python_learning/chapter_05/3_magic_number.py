answer = 17
if answer != 42:
	print('That is not the correct answer. Please try again!')
# Такой же пример как и в 2_toppings.py только с числами.

# Проверка нескольких условий(ниже).
age_0 = 22
age_1 = 18
if (age_0 >= 18) and (age_1 >=18):# True
	print('True')
else:
	print('False')
# and-говорится как 'и'. Чтобы проверить, что два условия истины ОДНОВРЕМЕННО, нужно объеденить их ключевым словом and; если оба условия истины,то и всё выражение тоже истино. Если хотя бы одно(или оба)условия ложны , то и результат всего выражения равен False.
# Чтбоы код лучше читался лучше заключить его в круглые скобки, но это не обязательно
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
	print('True')
else:
	print('False')
# or-говорится как 'или'. Результат общей проверки являестя истиным в том случае, когда истино хотябы одно или оба условия.

reguested_toppongs = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in reguested_toppongs:
	print('True')
else:
	print('False')
