import unittest
from worker import Employee

class WorkerTestCase(unittest.TestCase):
	"""Тесты для Employee."""
	def setUp(self):
		"""Создание экземпляра Employee и ответов."""
		self.worker = Employee('danil', 'lomakin', 120000)

	def test_give_default_raise(self):
		self.worker.give_raise()
		self.assertEqual(self.worker.salary, 125000)

	def test_give_custom_raise(self):
		self.worker.give_raise(10000)
		self.assertEqual(self.worker.salary, 130000)

unittest.main()
# Упражнение 11-3.
