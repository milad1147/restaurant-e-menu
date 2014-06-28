import time
import datetime
from config.globals import *
from .dbhandler import *
import json


class Session:

    def __init__(self, sid):
        self.sid = sid
        self.dbHandler = DbHandler.getInstance()
        self.cur = self.dbHandler.cur
        self.cur.execute("""SELECT data, expires FROM `user_session`
                    WHERE sid='{sid}'
                    """.format(sid=sid))
        if (self.cur.rowcount > 0):
            session = self.cur.fetchone()
            rawData = session[0]
            expires = time.mktime(session[1].timetuple())
            if (time.time() > expires):
                raise Exception('Session expired')
            if (rawData is None or rawData == ''):
                raise Exception('Invalid session')
            self.data = json.loads(session[0])
        else:
            self.cur.execute("""INSERT INTO `user_session` (sid, expires)
                    VALUES('{sid}', DATE_ADD( NOW( ) , INTERVAL 1 WEEK ))
                    """.format(sid=sid))
            self.dbHandler.conn.commit()
            self.data = {}

    def addData(self, key, value):
        self.data[key] = value
        self.__updateData()

    def deleteData(self, key):
        del(self.data[key])
        self.__updateData()

    def __updateData(self):
        self.cur.execute("""UPDATE `user_session`
                    SET `data` =  '{data}'
                    WHERE `sid` =  '{sid}';
                    """.format(sid=self.sid, data=json.dumps(self.data)))
        self.dbHandler.conn.commit()

    @staticmethod
    def destroy(sid):
        dbHandler = DbHandler.getInstance()
        dbHandler.cur.execute("""DELETE FROM `user_session`
                                WHERE `sid` =  '{sid}';
                                """.format(sid=sid))
        dbHandler.conn.commit()
