import unittest

from cars import *

class CarClassTest(unittest.TestCase):
    """docstring for CarClassTest"""

    def test_car_instance(self):
        honda = Car('Honda')
        self.assertIsInstance(honda, Car, msg='The object should be an instance of the `Car` class')