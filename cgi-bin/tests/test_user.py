import unittest
from model.user import *


class UserTest(unittest.TestCase):

    def test_instance(self):
        user = User('vankata', '123')
        self.assertEqual(user.username, 'vankata')
        self.assertEqual(user.userRoles, [1, 4])

    def test_wrong_pass(self):
        self.assertRaises(ValueError, User, 'vankata', '1234')
