import json


class Controller:
    def __init__(self):
        pass  # TODO

    def call(self, methodName, cgiFieldStorage):
        if self.checkPermissions(methodName):
            params = self.getInputParams(cgiFieldStorage)
            result = getattr(self, methodName)(params)
            return self.resultOut(result)

    def checkPermissions(self, methodName):
        return True

    def getInputParams(self, cgiFieldStorage):
        params = {}
        for key in cgiFieldStorage:
            params[key] = cgiFieldStorage.getvalue(key)
        return params

    def resultOut(self, data=None):
        result = {
            'success': True,
        }

        if data is not None:
            if isinstance(data, bool):
                result['status'] = data
            else:
                result['data'] = data
        return self.out(result)

    def out(self, result):
        return json.dumps(result)
