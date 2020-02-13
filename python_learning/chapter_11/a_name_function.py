def get_formated_name(first, last, middle=''):
	"""Строит отформатированное имя."""
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()

# "Сбой теста" стр. 213-214.

# "Реакция на сбойный тест" стр. 214-215.
