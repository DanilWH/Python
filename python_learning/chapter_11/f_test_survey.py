import unittest
from d_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Тесты для класса AnonymousSurvey"""

	def test_store_single_response(self):
		"""Проверяет, что один ответ сохранён правильно."""
		question = "What language did you first learn speak?"
		my_servey = AnonymousSurvey(question)
		my_servey.store_response('English')

		self.assertIn('English', my_servey.responses)

	def test_store_three_responses(self):
		"""Проверяет, что три ответа были созранены правильно."""
		question = "What language did you first learn speak?"
		my_servey = AnonymousSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']
		for response in responses:
			"""
			Цикл для каждого из ответов в списке responses, вызывает метод store_response.
			"""
			my_servey.store_response(response)

		for response in responses:
			"""
			Цикл проверяет что каждый ответ теперь присутствует в my_servey.responses.
			"""
			self.assertIn(response, my_servey.responses)

unittest.main()
# Чтобы протестировать поведение класса, необходимо создать экземпляр класса в в методе, который тестирует класс.

# "Тестирование класса AnonymousSurvey" стр.219-220.


import unittest
from d_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Тесты для класса AnonymousSurvey"""
	def setUp(self):
		"""
		Создание опроса и набора ответов для всех тестовых методов.
		"""
		question = "What language did you first learn speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']

	def test_store_single_response(self):
		"""Проверяет, что один ответ сохранён правильно."""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Проверяет, что три ответа были созранены правильно."""
		for response in self.responses:
			"""
			Цикл для каждого из ответов в списке responses, вызывает метод store_response.
			"""
			self.my_survey.store_response(response)

		for response in self.responses:
			"""
			Цикл проверяет что каждый ответ теперь присутствует в my_servey.responses.
			"""
			self.assertIn(response, self.my_survey.responses)

unittest.main()
# Класс unittest.TestCase содержит метод setUp(), который позволяет создавать эти объекты один раз, а затем использовать их в каждом из тестовых методов.

# Все объекты, созданные методом setUp(), становятся доступными во всех написаных тестовых методах.

# Метод setUp() решает две задачи: он создаёт экземпляр опроса и список ответов.

# Каждый из атрибутов снабжается префиксом self, поэтому он может использоваться где угодно в классе.

# Этот пример кода может не работать так как самый первый пример кода "перебивает" выполнение этого кода. Чтобы этот пример тестового сценария заработал, нужно стереть первый пример(только перед стиранием скопируй первый пример в блокнот, а потом уже стрирай и проверяй работоспособность второго примера кода.).