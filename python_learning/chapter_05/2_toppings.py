reguested_toppings = 'mushrooms'# "Грибы"

if reguested_toppings != 'anchovies':# "Анчоусы"
    print('Take yourself anchovies!\n')# "Возмите свои анчоусы!"
# Если нужно проверить, что два значения различны, надо использовать комбинацию из восклицательного знака и знака равенства(!=).

# Проверка нескольких условий, стр. 94-95.
reguested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in reguested_toppings:
	print('Adding mushrooms')# Добавление грибов.
if 'pepperoni' in reguested_toppings:
	print('Adding pepperoni')# Добавление пепперони.
if 'extra cheese' in reguested_toppings:
	print('Adding extra cheese')# Добавление экстра сыра.

print('Finished making your pizza!\n')
# Иногда бывает нужно проверить все условия, представляющие интерес. В таких случаях следует применять серии простых команд if без блоков elif или else.
# Такое решение уместно, когда истинным могут быть сразу несколько условий и надо отреагировать на все истинные условия.

# Если нужно, чтобы в программе выполнялся только один блок кода,-нужно использовать цепочку if-elif-else.
# Если же выполняться должны несколько блоков, нужно использовать серию независимых команд if.

# Проверка специальных значений стр.96-97.
reguested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for reguested_topping in reguested_toppings:
	if reguested_topping == 'green peppers':
		print('Sorry, we are out of green peppers right now.')
	else:
		print('Adding ' + reguested_topping + '.')

print('Finished making your pizza!')
# Допустоим что в пиццерии кончился зелёный перец.
# Комадна if в цикле for может правильно обработать эту ситуацию.
# Подробнее на стр.96-97.

reguested_toppings = []

if reguested_toppings:
	for reguested_topping in reguested_toppings:
		print('Adding ' + reguested_topping + '.')
	print('\nFinished making your pizza!')
else:
	print('\nAre you sure you want a plain pizza?\n')# Вы действительно хотите поростую пиццу?
# Когда имя списка используется в условии if, Python возвращает True, если содержит хотя бы один элемент; если список пуст, возвращается значение False.
# Если в списке есть хотя бы ожин элемент, в выходные данные включается каждое заказанное дополнение.
# Подробнее на стр.97-98. "Проверка наличия элементов в списке"

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

reguested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for reguested_topping in reguested_toppings:
	if reguested_topping in available_toppings:
		print('Adding ' + reguested_topping + '.')
	else:
		print('Sorry, we do not have ' + reguested_topping + '.')

print('Finished making pizza!')
# С этим синтаксисом программа выдаёт чёткий, содержательный ответ.
# Подробнее об этом на стр.98-99. "Множественные списки".
