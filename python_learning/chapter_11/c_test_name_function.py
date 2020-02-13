import unittest
from a_name_function import get_formated_name

class NamesTestCase(unittest.TestCase):
	"""Тесты для 'a_name_function.py'."""

	def test_first_last_name(self):
		"""Имена вида 'Danil Lomakin' работают правильно?"""
		formatted_name = get_formated_name('danil', 'lomakin')
		self.assertEqual(formatted_name, 'Danil Lomakin')

	def test_first_middle_last_name(self):
		"""Работают ли ьакие имена, как 'Wolfgang Amadeus Mozart'?"""
		formatted_name = get_formated_name('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
# Любой метод в классе, имя которого начинается с test_, будет выполняться автоматически при запуске c_test_name_function.py.
# Методы assert проверяют, что полученный результат соответствует тому результату, который расчитывали получить.
# Строка self.assertEqual(formatted_name, 'Danil Lomakin') означает: "Сравни значение formatted_name со строкой 'Danil Lomakin'. Если они равны, как и ожидалось,-хорошо. Но если они не равны, обязательно сообши мне!"
# Строка unittest.main() приказывает Python выполнить тесты из этого файла.
# "Прохождение теста" стр. 211-213.

# "Сбой теста" стр. 213-214.

# "Реакция на сбойный тест" стр. 214-215.

# Чтобы протестировать программу и с именем и фамилеей, и с именем, вторым иминем и фамилией, нужно добавить ещё одим метод тестирующий соответсвующую функцию.
# "Добавление новых тестов"стр. 215-216.
