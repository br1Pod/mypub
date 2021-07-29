import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Withnail", 45)
        self.customer2 = Customer("Marwood", 32)
        self.customer3 = Customer("Jake the Poacher", 62)

        self.drink1 = Drink("Whiskey", 3.25)
        self.drink2 = Drink("Large Gin", 4.10)
        self.drink3 = Drink("Cider", 2.75)
