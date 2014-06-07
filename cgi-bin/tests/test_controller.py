import unittest
from controller.admin import *


class ControllerTest(unittest.TestCase):

    def test_call_with_unexisting_method(self):
        self.adminController = AdminController()
        self.assertRaises(Exception, self.adminController.call, 'unexistingMethod', None)
