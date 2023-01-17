from datetime import datetime
from behave import *
import requests
import json
BASE_URL = "http://lms-backend-service.herokuapp.com/lms/saveprogram"
#file= open ("program.json","r")
#json_input=file.read()
#request_json=json.loads(json_input)

programdata={
 "programName": "Jan16-NinjaSurvivors-5-SDET-80",
 "programDescription": "LMS-Hackathon-SDET-NinjaSurvivors-5",
 "programStatus": "Active",
 "creationTime": datetime,
 "lastModTime": datetime
    }

request_json=json.loads(programdata)
#response=requests.post(BASE_URL,request_json)
response = requests.post(BASE_URL,programdata)
print(response.content)
print(str(response['programName']))
print(str(response['programDescription']))


#print(response.toJSON())

#print(type(response))
#res=requests.post(BASE_URL,data=response)
#print(res)
#print(res.json())


#myjsonfile=open('jsonFiles/employee.json','r')
