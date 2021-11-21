import unittest
from testex1 import cityfunction

# class Testing_cities(unittest.TestCase):
#     def test_city_testing(self):
#         formatted_cityName=cityfunction('Santiago','Chile')
#         self.assertEqual(formatted_cityName,'Santiago Chile')
# if __name__=='__main__':
#     unittest.main()

# second test

class Testing_cities_population(unittest.TestCase):
    def test_cities_population(self):
        formatted_details=cityfunction('Santiago','Chile','0.5M')
        self.assertEqual(formatted_details,'Santiago Chile - population 0.5M')
