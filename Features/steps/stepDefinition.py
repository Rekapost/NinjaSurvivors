from behave import *
import requests
import json
BASE_URL = "http://lms-backend-service.herokuapp.com/lms"

@given(u'user makes request with url')
def step_impl(context):
    BASE_URL = "http://lms-backend-service.herokuapp.com/lms"

@when(u'user makes get request for get all programs , all programs are displayed , status code is verified')
def step_impl(context):
    response1 = requests.get(BASE_URL + "/allPrograms")
  #  print(json.dumps(response1.json(), indent=4))
    code = response1.status_code
    assert code == 200, " code does not match"

@when(u'user makes get request to get program by id,user get a particular program by id')
def step_impl(context):
    response2 = requests.get(BASE_URL + "/programs/8119")
    print(json.dumps(response2.json(), indent=4))
    code = response2.status_code
    assert code == 200, " code does not match"


@when(u'user makes request to get program by name,user gets particular program by name')
def step_impl(context):
    BASE_URL = "http://lms-backend-service.herokuapp.com/lms"


@when(u'user makes  request to  delete program by id, progarm is deleted')
def step_impl(context):
    BASE_URL = "http://lms-backend-service.herokuapp.com/lms"


@when(u'user makes get request for get all batches,Then  user gets  all batches')
def step_impl(context):
    response4 = requests.get(BASE_URL + "/batches")
 #   print(json.dumps(response4.json(), indent=4))
    code = response4.status_code
    assert code == 200, " code does not match"


@when(u'user makes get request to get batch by id,Then user get a particular batch by id')
def step_impl(context):
    response5 = requests.get(BASE_URL + "/batches/batchId/2326")
    print(json.dumps(response5.json(), indent=4))
    code = response5.status_code
    assert code == 200, " code does not match"


@when(u'user makes request to get batch by name,Then user gets particular batch by name')
def step_impl(context):
    response6 = requests.get(BASE_URL + "/batches/batchName/Jan23-Ninjasurvivors-SDET-SDET94-01")
    print(json.dumps(response6.json(), indent=4))
    code = response6.status_code
    assert code == 200, " code does not match"


@when(u'user makes  request to  delete batch by id,Then batch is deleted')
def step_impl(context):
    response7 = requests.delete(BASE_URL + "/batches/2326")
    print(json.dumps(response7.json(), indent=4))
    code = response7.status_code
    assert code == 200, " code does not match"



