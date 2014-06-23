from .controller import *
from model.item import *
from model.category import *


class AdminController(Controller):

    def getAllItems(self, params):
        return Item.getAllItems()

    def getCategories(self, params):
        return Category.getTree()
