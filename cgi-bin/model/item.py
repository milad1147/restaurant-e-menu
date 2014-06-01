from .db import *


class Item:

    def __init__(self, id):
        pass  # TODO

    @staticmethod
    def getAllItems():
        cur.execute("SELECT * FROM item")
        return cur.fetchall()
