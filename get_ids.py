import requests
import json

personId = []

key = '{Ocp-Apim-Subscription-Key}' #YOUR key. Not gonna give you mine, smartypants

def get_ids(personId, key):
  headers = {'Ocp-Apim-Subscription-Key': key}
  params = {'top': '100'} #return up to 100 people in personGroup

  resp_get_ids = requests.get("https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}/persons?",
                              params = params,
                              headers = headers)

  data = json.loads(resp_get_ids.text) #transform it into json

  for i in range(len(data)):
    personId.append([data[i]["personId"],data[i]["name"]]) #add to list the personId and its name as a list

  print(personId)

get_ids(personId, key)
