import task11_1
import unittest


class CCTest(unittest.TestCase):
    def test_country_city(self):
        country_city = 'Xian,China'
        self.assertEqual(country_city, task11_1.country_city('china', 'xian'))

