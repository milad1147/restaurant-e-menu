import cgi
import json
from controller.admin import *
from config.classes import *


className = 'admin'  # this will be Post param
methodName = 'getAllItems'  # this will be Post param

controller = classes[className]()
result = controller.call(methodName)
print()
print(json.dumps(result))

cur.close()
conn.close()
