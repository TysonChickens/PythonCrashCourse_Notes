import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        city_country = get_city_country('portland', 'united states')
        self.assertEqual(city_country, "Portland, United States")

    def test_city_country_population(self):
        city_country_population = get_city_country('santiago', 'chile', population=5000000)
        self.assertEqual(city_country_population, "Santiago, Chile - Population 5000000")

if __name__ == '__main__':
    unittest.main()