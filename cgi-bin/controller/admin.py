from .controller import *
from model.item import *
from model.category import *


class AdminController(Controller):

    def getAllItems(self, params):
        if "category_id" in params.keys():
            return Item.getAllItemsInCat(params["category_id"])
        else:
            return Item.getAllItems()

    def getCategories(self, params):
        return Category.getTree()

    def updateCategory(self, params):
        keys = ('name', 'description', 'parent')
        catData = {k: v for k, v in params.items() if k in keys}
        cat = Category(params['id'])
        cat.set(**catData)
        cat.save()

    def addCategory(self, params):
        keys = ('name', 'description', 'parent')
        catData = {k: v for k, v in params.items() if k in keys}
        cat = Category()
        cat.set(**catData)
        cat.save()

    def deleteCategory(self, params):
        cat = Category(params['id'])
        return cat.delete()
