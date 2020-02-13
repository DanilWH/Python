import unittest

from country_codes import get_country_code

class CodesTestCase (unittest.TestCase):
    """Tests for get_country_code()"""

    def test_get_country_code(self):
        """Countries of type 'Niger' should returns 'ne'."""
        code = get_country_code('Niger')
        self.assertEqual(code, 'ne')

        code = get_country_code('Liberia')
        self.assertEqual(code, 'lr')

        code = get_country_code('Greece')
        self.assertEqual(code, 'gr')

unittest.main()