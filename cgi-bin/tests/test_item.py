import unittest
from model.item import *


class ItemTest(unittest.TestCase):

    def test_getAllItems(self):
        self.items = Item.getAllItems()
        self.assertIsInstance(self.items, list)
        self.assertTrue(len(self.items) > 0, 'No items were read from the DB')