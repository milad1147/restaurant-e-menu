from .controller import *
from model.item import *
from model.category import *


import os
from http import cookies
from model.session import *


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

    def checkPermissions(self, methodName):
        administratorMethods = [
            'addCategory',
            'deleteCategory',
            'updateCategory',
            'addItem',
            'deleteItem',
            'updateItem'

        ]
        waitersMethods = []
        if methodName in administratorMethods:
            string_cookie = os.environ.get('HTTP_COOKIE')
            if string_cookie:
                cookie = cookies.SimpleCookie()
                cookie.load(string_cookie)
                if 'sid' in cookie.keys():
                    sid = cookie['sid'].value
                    session = Session(sid)
                    if 'userRoles' in session.data.keys():
                        userRoles = session.data['userRoles']
                        if methodName in administratorMethods and 1 in userRoles:
                            return True
                        if methodName in waitersMethods and (1 in userRoles or 2 in userRoles):
                            return True
            raise PermissionError('Access denied!')
        else:
            return True
