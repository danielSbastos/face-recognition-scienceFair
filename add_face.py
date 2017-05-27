import requests
import json

'''ADD FACES TO CERTAIN PERSON (INCLUDE PERSONID) '''

key = "{Ocp-Apim-Subscription-Key}" #YOUR key. Not gonna give you mine, smartypants

personId = input("Person ID: ") #define person whose faces will be added
number_files = int(input("Number of files: ")) #define number number of files (faces) to add

files = []
for i in range(number_files):
	files.append(input("File: ")) #append all files to a list


def detect(i, key):
  headers_octet = {
      'Content-Type': 'application/octet-stream',
      'Ocp-Apim-Subscription-Key': key}

  params = {'returnFaceId': 'true',
            'returnFaceLandmarks' : 'true'}

  resp_detect = requests.post("https://westus.api.cognitive.microsoft.com/face/v1.0/detect?%",
                              params = params,
                              data = open(i, 'rb'),
                              headers = headers_octet)

  data = json.loads(resp_detect.text)
  #define face rectangle coordinates as "targetFace"
  targetFace = str(data[0]['faceRectangle']["left"])+","+str(data[0]['faceRectangle']["top"])+","+ \
              str(data[0]['faceRectangle']["width"])+","+str(data[0]['faceRectangle']["height"])

  return targetFace #targetFace will be used in add_face function below


def add_face(i, personId):
  headers_octet = {
      'Content-Type': 'application/octet-stream',
      'Ocp-Apim-Subscription-Key': key}

  params = {'targetFace': detect(i, key)} #call detect function and get targetFace of each photo/face

  url = "https://westus.api.cognitive.microsoft.com/face/v1.0" #just for the sake of splitting it into 2 lines
  url2 = "/persongroups/{personGroupId}/persons/"+personId+"/persistedFaces?%"

  resp_add_face = requests.post(url+url2, params = params, data = open(i, 'rb'), headers = headers_octet)

  data = json.loads(resp_add_face.text)
  print(data) #return response as json


for i in files: #for all the files with faces added by the user, execute the defined functions
	add_face(i, personId)
