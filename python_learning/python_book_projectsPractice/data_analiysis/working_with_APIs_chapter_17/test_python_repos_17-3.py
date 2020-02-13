import unittest

import python_repos as pr

class TestRightData(unittest.TestCase):
    """Тесты, проверяющие успешный вызов API и правильность данных."""

    def setUp(self):
        self.r = pr.get_adress()
        self.response_dict = pr.get_dict_info(self.r)

    def test_status_code(self):
        self.assertEqual(self.r.status_code, 200)

    def test_len_repos(self):
        self.assertEqual(len(self.response_dict['items']), 30)

    def test_len_total_repos(self):
        self.assertTrue(self.response_dict['total_count'] >= 4_000_000)

    def test_incomplete_results(self):
        self.assertFalse(self.response_dict['incomplete_results'])

unittest.main()