from behave import *
import allure
import pytest
from allure_commons.types import AttachmentType
#@allure.severity(allure.severity_level.NORMAL)   decorators class level
#@allure.severity(allure.severity_level.BLOCKER)

import requests
import json
BASE_URL = "http://lms-backend-service.herokuapp.com/lms"
response=requests.get(BASE_URL+"/allPrograms")
print(response)
print(response.json())
print(json.dumps(response.json(),indent=4))
code=response.status_code
assert code==200," code does not match"

payload={
 "programName": "Jan16-NinjaSurvivors-5-SDET-80",
 "programDescription": "LMS-Hackathon-SDET-NinjaSurvivors-5",
 "programStatus": "Active",
 "creationTime": "2023-01-17T00:18:37.958+00:00",
 "lastModTime": "2023-01-17T00:18:37.958+00:00"
}
#pytest -v -s AllureReportsDemo/test_nopCommerce.py
# pytest -v -s --alluredir="C:\Users\Reka\PycharmProject\PythonAllureReports\AllureReportsDemo\reports"

#pytest -v -s --html=Report.html pytesthtmlReport/test_nopCommerce.py
#pytest -v -s C:\Users\Reka\PycharmProject\pytestHTMLreport\pytesthtmlReport\test_nopCommerce.py

#pytest -v -s C:\Users\Reka\PycharmProject\ninjaSurvivors\pytestReport\allPrograms.py
#pytest -v -s --html=Report.html --self-contained-html pytesthtmlReport/allPrograms.py

#pytest -v -s pytestReport/test_nopCommerce.py

#   pytest -v -s C:\Users\Reka\PycharmProject\ninjaSurvivors\pytsetReport\allPrograms.py
# OR
#   pytest -v -s pytesthtmlReport/test_nopCommerce.py

#Report Generation
#   pytest -v -s --html=Report.html pytesthtmlReport/test_nopCommerce.py
# OR
#   pytest -v -s --html=Report.html --self-contained-html pytesthtmlReport/test_nopCommerce.py