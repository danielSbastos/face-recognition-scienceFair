import httplib, urllib, base64
import ast


'''ADD FACES TO CERTAIN PERSON (INCLUDE PERSONID) '''


global personId
personId = raw_input("Person ID: ") #personId for the person the faces are being added to


number_files = input("Number of files: ")

files = []
for i in range(number_files):
	files.append(raw_input("File: ")) #if file not in file root directory, specify the directory of the file


global headers_octet
headers_octet = {
    	'Content-Type': 'application/octet-stream',
    	'Ocp-Apim-Subscription-Key': '{subscription-key}',
		}



def detect(i):
	params = urllib.urlencode({
    	'returnFaceId': 'true',
    	'returnFaceLandmarks': 'false'
		})

	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn.request("POST", "/face/v1.0/detect?%s" % params, open(i, 'rb'), headers_octet)
	response = conn.getresponse()


	data = response.read()
	data = ast.literal_eval(data)

	targetFace = str(data[0]['faceRectangle']["left"])+","+str(data[0]['faceRectangle']["top"])+","+str(data[0]['faceRectangle']["width"])+","+str(data[0]['faceRectangle']["height"])

	conn.close()

	return targetFace


def add_face(i):
	params1 = urllib.urlencode({
    	'targetFace': detect(i)     
    	})

	conn1 = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn1.request("POST", "/face/v1.0/persongroups/{groupPersonId}/persons/"+ personId+"/persistedFaces?%s" % params1, open(i, 'rb'), headers_octet)
	response1 = conn1.getresponse()

	data1 = response1.read()
	conn1.close()

	print(data1)


for i in files:
	add_face(i)
