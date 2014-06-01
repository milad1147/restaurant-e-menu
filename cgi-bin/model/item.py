from .db import *


class Item:

    def __init__(self, id):
        pass  # TODO

    @staticmethod
    def getAllItems():
        cur.execute("SELECT name, price, short_description FROM item")
        items = []
        for item in cur.fetchall():
            items.append({
                'name': item[0],
                'short_description': item[2],
                'price': float(item[1])
            })
        return items
