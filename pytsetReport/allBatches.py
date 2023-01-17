from behave import *
import requests
import json
BASE_URL = "http://lms-backend-service.herokuapp.com/lms"
response=requests.get(BASE_URL+"/batches")
print(response)
print(response.json())
print(json.dumps(response.json(),indent=4))
code=response.status_code
assert code==200," code does not match"