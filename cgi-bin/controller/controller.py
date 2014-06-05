class Controller:
    def __init__(self):
        pass  # TODO

    def call(self, methodName, params):
        if self.checkPermissions(methodName):
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
