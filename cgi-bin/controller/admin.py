from .controller import *
from model.item import *


class AdminController(Controller):

    def getAllItems(self, params):
        return Item.getAllItems()
