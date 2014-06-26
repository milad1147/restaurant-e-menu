from collections import defaultdict
from .dbhandler import *


class Category:

    def __init__(self, catId=None):
        self.dbh = DbHandler.getInstance()
        self.cur = self.dbh.cur

        if catId is not None:
            query = """SELECT
                            name,
                            description,
                            ifnull(parent_category,0)
                        FROM category
                        WHERE id_category = {catId}
                        LIMIT 1
                    """.format(catId=catId)
            self.cur.execute(query)
            if (self.cur.rowcount == 0):
                raise ValueError("Item not found!")

            row = self.cur.fetchone()
            self.id = catId
            self.name = row[0]
            self.parent = row[2]
            self.description = row[1]
        else:
            self.id = None
            self.id = catId
            self.parent = 0
            self.description = ''

    def set(self, **kwargs):
        for key, val in kwargs.items():
            if key != 'id':
                self.__setattr__(key, val)

    def save(self):
        if int(self.parent) == 0:
            self.parent = 'NULL'

        if self.id is None:
            query = """INSERT INTO category
                        SET name = '{name}',
                            description = '{description}',
                            parent_category = {parent}
            """.format(
                name=self.name,
                description=self.description,
                parent=self.parent
            )
        else:
            query = """UPDATE category
                        SET name = '{name}',
                            description = '{description}',
                            parent_category = {parent}
                        WHERE id_category = {catId}
            """.format(
                catId=self.id,
                name=self.name,
                description=self.description,
                parent=self.parent
            )
        self.cur.execute(query)
        self.dbh.conn.commit()

    def delete(self):
        if self.id is not None:
            query = """DELETE FROM category
                        WHERE id_category = {catId}
                        LIMIT 1
            """.format(catId=self.id)
            self.cur.execute(query)
            self.dbh.conn.commit()
            return query

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
                    'name': category['name'],
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
