import printing_functions

# Список моделей, которые необходимо напечатать.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Цикл последовательно печатает каждую модель до конца списка.
# После печати каждая модель перемещается в список comleted_models.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	# Печать модели на 3D принтере.
	print("Printing model: " + current_design)
	completed_models.append(current_design)

# Вывод всех готовых моделей.
print("\nThe following models have been printed:")
for completed_models in completed_models:
	print(completed_models)
# Пример без функций(перемещения элементов из одного списка в другой).

print(" ")

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
# Пример с функцией(перемещения элементов из одного списка в другой).
# Такой пример более правильный и лучше читается.
