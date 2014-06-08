from .dbhandler import *


class User:

    def __init__(self, username, password):
        dbh = DbHandler.getInstance()
        cur = dbh.cur
        cur.execute("""SELECT ur.id_role FROM `uers` AS u
                    RIGHT JOIN `user_roles` AS ur ON u.id_user = ur.id_user
                    WHERE username='{username}' and password=sha1({password})
                    """.format(username=username, password=password))
        if (cur.rowcount > 0):
            userRoles = []
            for row in cur.fetchall():
                userRoles.append(row[0])

            self.username = username
            self.userRoles = userRoles
        else:
            raise ValueError
