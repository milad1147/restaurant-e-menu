import unittest
from model.session import *
from model.dbhandler import *


class SessionTest(unittest.TestCase):

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

    def test_destroy(self):
        session = Session('123')
        session.addData('key', 'vall')

        Session.destroy('1234')
        Session.destroy('123')
        dbh = DbHandler.getInstance()
        cur = dbh.cur

        cur.execute("""SELECT data FROM `user_session`
                    WHERE sid IN ('123', '1234')""")
        self.assertEqual(cur.rowcount, 0)
