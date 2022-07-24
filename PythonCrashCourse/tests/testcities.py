import unittest
from city_function import create_city


class CreateCityTest(unittest.TestCase):

    def test_country_city(self):
        result = create_city('Chile', 'Santiago', 500_000_0)
        self.assertEqual(result, 'Chile, Santiago - population: 5000000')


if __name__ == '__main__':
    unittest.main()