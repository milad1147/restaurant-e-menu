class Controller:
    def __init__(self):
        pass  # TODO

    def call(self, methodName, cgiFieldStorage):
        if self.checkPermissions(methodName):
            params = self.getInputParams(cgiFieldStorage)
            result = getattr(self, methodName)(params)
            return {
                'status': True,
                'data': result
            }
        else:
            return {
                'status': False,
                'message': 'access denied'
            }

    def checkPermissions(self, methodName):
        return True

    def getInputParams(cgiFieldStorage):
        params = {}
        for key in cgiFieldStorage:
            params[key] = cgiFieldStorage.getvalue(key)
        return params
