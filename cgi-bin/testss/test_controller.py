import unittest
from controller.admin import *


class SimpleWidgetTestCase(unittest.TestCase):

    def test_call_with_unexisting_method(self):
        self.adminController = AdminController()
        self.result = self.adminController.call('unexistingMethod')
        self.assertFalse(self.result['status'])


if __name__ == '__main__':
    unittest.main()
