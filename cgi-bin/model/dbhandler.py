import pymysql
from config.globals import *


class DbHandler:
    instance = None

    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user=mysqlUser,
            passwd=mysqlPass,
            db=dataBase,
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    @staticmethod
    def getInstance():
        if (DbHandler.instance is not None):
            return DbHandler.instance
        else:
            DbHandler.instance = DbHandler()
            return DbHandler.instance

    @staticmethod
    def close():
        if (DbHandler.instance is not None):
            DbHandler.instance.cur.close()
            DbHandler.instance.conn.close()
