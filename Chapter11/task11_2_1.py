import unittest
import task11_2


class CCPTest(unittest.TestCase):
    def test_cc(self):
        result = 'Xian,China'
        self.assertEqual(result, task11_2.country_city('china', 'xian'))

    def test_ccp(self):
        result = 'Xian,China - population 10000'
        self.assertEqual(result, task11_2.country_city('china', 'xian', population=10000))
