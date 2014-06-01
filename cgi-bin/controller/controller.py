class Controller:
    def __init__(self):
        pass  # TODO

    def call(self, methodName, *params):
        if self.checkPermissions(methodName):
            return getattr(self, methodName)(*params)
        else:
            return False

    def checkPermissions(self, methodName):
        return True
