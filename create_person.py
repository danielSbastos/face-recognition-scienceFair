import httplib, urllib, base64
import ast

'''CREATE PERSON AT SPECIFIC GROUP PERSON '''

def create_person():
	headers = {
    	'Content-Type': 'application/json',
    	'Ocp-Apim-Subscription-Key': '{subscription-key}',
		}


	name = "'" + raw_input("Insert person's name: ") + "'"
	body = "{'name':" + name + "}"

	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn.request("POST", "/face/v1.0/persongroups/{personGroupId}/persons?", body, headers)
	response = conn.getresponse()

	data = response.read()
	personId = ast.literal_eval(data)
	personId = personId["personId"]

	conn.close()
	print personId

create_person()
