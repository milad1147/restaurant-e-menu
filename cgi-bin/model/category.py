from collections import defaultdict
from .dbhandler import *


class Category:

    def __init__(self, id):
        pass  # TODO

    @staticmethod
    def getTree():
        dbh = DbHandler.getInstance()
        cur = dbh.cur
        cur.execute("""SELECT
                         id_category,
                         name,
                         ifnull(parent_category,0)
                        FROM category
                        ORDER BY parent_category ASC""")
        categories = []
        for category in cur.fetchall():
            categories.append({
                'id': category[0],
                'name': category[1],
                'parent': category[2],
            })
        return Category.parseTree(categories, 0)

    @staticmethod
    def parseTree(tree, root):
        # http://stackoverflow.com/questions/2915748/how-can-i-convert-a-series-of-parent-child-relationships-into-a-hierarchical-tre
        result = []
        for i in range(0, len(tree)):
            category = tree[i]
            if category['parent'] == root:
                data = Category.parseTree(tree, category['id'])
                cat = {
                    'id': category['id'],
                    'catName': category['name'],
                }
                if data is not None:
                    cat['data'] = data
                else:
                    cat['leaf'] = True
                result.append(cat)
        if len(result) == 0:
            return None
        else:
            return result
