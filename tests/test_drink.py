import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Whiskey", 3.25)
        self.drink2 = Drink("Large Gin", 4.10)
        self.drink3 = Drink("Cider", 2.75)