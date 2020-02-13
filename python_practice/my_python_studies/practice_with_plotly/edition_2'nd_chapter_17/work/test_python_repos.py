"""
    17-3. Testing python_repos_visual.py:
"""

import unittest

import python_repos_visual as prv

class TestNeededData(unittest.TestCase):
    """Tests for python_repos_visual.py"""

    def setUp(self):
        self.r = prv.get_url()
        self.response_dict = prv.get_dict(self.r)
        self.repo_dicts = self.response_dict['items']

    def test_status_code(self):
        self.assertEqual(self.r.status_code, 200)

    def test_lenght_most_popular_projects(self):
        self.assertEqual(len(self.repo_dicts), 30)

    def test_overall_number_repositories(self):
        self.assertTrue(self.response_dict['total_count'] > 4_000_000)

    def test_complete_results(self):
        self.assertFalse(self.response_dict['incomplete_results'])

    def test_data_presence(self):
        datas = ['name', 'html_url', 'stargazers_count', 'owner',
            'description']

        for repo_dict in self.repo_dicts:
            for data in datas:
                self.assertIn(data, repo_dict.keys())
                
                if data == 'owner':
                    self.assertIn('login', repo_dict['owner'].keys())

unittest.main()