from collections import defaultdict
from .dbhandler import *


class Category:

    def __init__(self, params):
        pass  # TODO

    @staticmethod
    def getTree():
        dbh = DbHandler.getInstance()
        cur = dbh.cur
        cur.execute("""SELECT
                         id_category,
                         name,
                         description,
                         ifnull(parent_category,0)
                        FROM category
                        ORDER BY parent_category ASC""")
        categories = []
        for category in cur.fetchall():
            categories.append({
                'id': category[0],
                'name': category[1],
                'description': category[2],
                'parent': category[3],
            })
        return Category.parseTree(categories, 0)

    @staticmethod
    def parseTree(tree, root):
        result = []
        for i in range(0, len(tree)):
            category = tree[i]
            if category['parent'] == root:
                data = Category.parseTree(tree, category['id'])
                cat = {
                    'id': category['id'],
                    'catName': category['name'],
                    'description': category['description'],
                    'parent': category['parent']
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
