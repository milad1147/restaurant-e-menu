import unittest
from model.item import *


class SimpleWidgetTestCase(unittest.TestCase):

    def test_getAllItems(self):
        self.items = Item.getAllItems()
        self.assertIsInstance(self.items, list)
        self.assertTrue(len(self.items) > 0, 'No items were read from the DB')


if __name__ == '__main__':
    unittest.main()
