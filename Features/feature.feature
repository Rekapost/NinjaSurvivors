Feature: verify the Request in the API

Scenario: Hit request and get response and validate with status code
	Given user makes request with url

	When user makes get request for get all programs , all programs are displayed , status code is verified

	When user makes get request to get program by id,user get a particular program by id

	When user makes request to get program by name,user gets particular program by name

	When user makes  request to  delete program by id, progarm is deleted


	When user makes get request for get all batches,Then  user gets  all batches

	When user makes get request to get batch by id,Then user get a particular batch by id

	When user makes request to get batch by name,Then user gets particular batch by name

	When user makes  request to  delete batch by id,Then batch is deleted



#Scenario: GET Request to get all programs
#  	 Given user make a service request with a base URL
#  	 When User make a GET request with an end point allProgram
#  	 Then User get the status code as 200 and got a response body as programID, programName, programDescription, programStatus, creationTime, lastModTime
#  	 And all programs are displayed
#		Then Validate respose "<status code>"
#	Examples:
#		|url			|statusCode|
#		|/saveprogram 	|201	   |
#		|/allProgram	|200		|

# behave Features\feature.feature