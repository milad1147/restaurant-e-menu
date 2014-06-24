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
