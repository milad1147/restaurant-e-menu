import cgi
import json
from controller.admin import *
from config.classes import *

params = cgi.FieldStorage()
className = params.getfirst("controllerClass", "admin")
methodName = params.getfirst("method", "getAllItems")

try:
    controller = classes[className]()
    result = controller.call(methodName, params)
except Exception as e:
    result = {'status': False, 'message': str(e)}

DbHandler.close()
print()
print(json.dumps(result))
