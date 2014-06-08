import unittest
from model.session import *


class UserTest(unittest.TestCase):

    def test_instance(self):
        session = Session('123')
        session.addData('key', 'vall')
        self.assertNotEqual(session.data, None)

    def test_add_data(self):
        session1 = Session('1234')
        session1.addData('testKey', 'testVal')
        session1.addData('list', ['val1, val2'])
        session2 = Session('1234')
        self.assertEqual(session1.data, session2.data)
