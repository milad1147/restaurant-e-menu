from .dbhandler import *


class Item:

    def __init__(self, id):
        pass  # TODO

    @staticmethod
    def getAllItems():
        dbh = DbHandler.getInstance()
        cur = dbh.cur
        cur.execute("SELECT id_item, name, short_description, price FROM item")
        items = []
        for item in cur.fetchall():
            items.append({
                'id': item[0],
                'name': item[1],
                'short_description': item[2],
                'price': float(item[3])
            })
        return items
