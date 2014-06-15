import cgi
import json
from config.classes import *

cgiFieldStorage = cgi.FieldStorage()
className = cgiFieldStorage.getfirst("controllerClass", "admin")
methodName = cgiFieldStorage.getfirst("method", "getAllItems")

try:
    controller = classes[className]()
    result = controller.call(methodName, cgiFieldStorage)
except Exception as e:
    result = json.dumps({'status': False, 'message': str(e)})

DbHandler.close()
print("Content-Type: text/json;charset=utf-8")
print()
print(result)
