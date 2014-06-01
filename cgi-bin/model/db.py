import pymysql
from config.globals import *

conn = pymysql.connect(host='localhost', port=3306, user=mysqlUser,
                            passwd=mysqlPass, db=dataBase, charset='utf8')
cur = conn.cursor()
