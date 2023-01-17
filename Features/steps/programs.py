from behave import *
import requests
import json
#BASE_URL = "http://lms-backend-service.herokuapp.com/lms"
#response=requests.get(BASE_URL+"/allPrograms")
# print(response)
# print(response.json())
#print(json.dumps(response.json(),indent=4))
#code=response.status_code
#assert code==200," code does not match"

url=BASE_URL = "http://lms-backend-service.herokuapp.com/lms/saveprogram"
file= open ("C://Users//Reka//Desktop//NumpyNinja//Ninja Survivors//info.json","r")
json_input=file.read()
request_json=json.loads(json_input)
print(request_json)

response=requests.post(url,request_json)
print(response.content)

# response = requests.get(BASE_URL + "/Programs/16Jan-NinjaSurvivors-2-SDET-710")
# print(json.dumps(response.json(), indent=4))
# code = response.status_code
# assert code == 200, " code does not match"


response3 = requests.delete(BASE_URL + "/deletebyprogid/6920")
print(json.dumps(response3.json(), indent=4))
code = response3.status_code
assert code == 200, " code does not match"