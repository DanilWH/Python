import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
	"""Тесты для названий городов и стран."""
	def test_city_country(self):
		"""Тестирует правильность форматирования названия города и страны."""
		formatted_name = get_city_country('Los-Angeles', 'American')
		self.assertEqual(formatted_name, 'Los-Angeles American.')

	def test_city_country_population(self):
		"""
		Тестирует правильность форматирования названия города, страны и населения.
		"""
		formatted_name = get_city_country('Los-Angeles', 'American', population=3000000)
		self.assertEqual(formatted_name, 'Los-Angeles American-population 3000000.')

unittest.main()
# Упражнение 11-1 и 11-2.
