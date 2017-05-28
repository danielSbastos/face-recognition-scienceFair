import requests
import json
import sys

'''CREATE PERSON'''

key = "{Ocp-Apim-Subscription-Key}" #YOUR key. Not gonna give you mine, smartypants

def create_person(key):
	headers = {
    	'Content-Type': 'application/json',
    	'Ocp-Apim-Subscription-Key': key}

	name = "'" + sys.argv[1] + ' ' +  sys.argv[2] + "'" #define person's name
	body = "{'name':" + name + "}" #add it to body part of request

	resp = requests.post("https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}/persons?",
										data = body,
										headers = headers)

	data = json.loads(resp.text) #transform to json
	print(data) #print response

create_person()



