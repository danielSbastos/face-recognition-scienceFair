''' TAKE PHOTO WITH WEBCAM AND COMPARE WITH GROUP PERSON TO FIND SIMILAR PERSON '''

#Librabries to draw on faces
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

#Libraries for API connection
import httplib, urllib, base64
import ast
import json

#Libraries to take photo with webcam
import pygame
import pygame.camera
from pygame.locals import *

##################################################################################

#Info to save webcam photo
global FILENAME
FILENAME = '{file-name}.jpg' #file taken by webcam will be saved with this name and later be used for analysis
DEVICE = '/dev/video0' #webcam port
SIZE = (640, 480) #resolution of pygame webcam window size

global targetFace
targetFace = []

global faceLandmarks
faceLandmarks = []

personId = []

def get_ids(personId):
	headers = {
    	'Ocp-Apim-Subscription-Key': '{subscription-key}',
		}

	params = urllib.urlencode({
    'top': '100', #only top 100 people will be shown in response
	})

	body = "{}"

	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	#making a GET request, not a POST one
	conn.request("GET", "/face/v1.0/persongroups/{personGroupId}/persons?%s" % params, body, headers)
	response = conn.getresponse()

	data = response.read()
	data = json.loads(data)

	for i in range(len(data)):
		#append to list the person id with its correspondant name, e.g. [124534nbh424523n5, Gabriel]
		personId.append([data[i]["personId"],data[i]["name"]])

	conn.close()


def camstream():
	#initialize camera and pygame
    pygame.init()
    pygame.camera.init()

    #initialize a window or screen for display
    display = pygame.display.set_mode(SIZE, 0)

    #load a camera and initialize it
    camera = pygame.camera.Camera(DEVICE, SIZE)
    camera.start()

    #call surface to represent display
    screen = pygame.surface.Surface(SIZE, 0, display)

    capture = True
    while capture:
    	#captures screen as a Surface
        screen = camera.get_image(screen)
        #update the full display Surface to the screen (previously only )
        display.blit(screen, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT: #if "x" button is present, finish capture and don't save the image
                capture = False
            elif event.type == KEYDOWN and event.key == K_s: #if "s" key is pressed, save photo and finish capture
                pygame.image.save(screen, FILENAME)
                capture = False

                
    camera.stop()
    pygame.quit()
    return

def detect():#will only open local images, do not type image's link.
	headers_octet = {
    	'Content-Type': 'application/octet-stream',
    	'Ocp-Apim-Subscription-Key': '{subscription-key}',
		}

	params = urllib.urlencode({
    	'returnFaceId': 'true',
    	'returnFaceLandmarks': 'true'
		})

	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn.request("POST", "/face/v1.0/detect?%s" % params, open(FILENAME, 'rb'), headers_octet)
	response = conn.getresponse()
	data = response.read()

	#turn string into dictionary
	data = ast.literal_eval(data)
	#select faceId and transform it string
	faceId = str(data[0]["faceId"])

	#append face rectangle coordinates
	targetFace.append(data[0]['faceRectangle']["left"])
	targetFace.append(data[0]['faceRectangle']["top"])
	targetFace.append(data[0]['faceRectangle']["width"])
	targetFace.append(data[0]['faceRectangle']["height"])

	#append each face landmarks, e.g. right and left pupil coordenates
	face_landmarks = data[0]['faceLandmarks']
	for sub_landmarks in face_landmarks:
		faceLandmarks.append(face_landmarks[sub_landmarks])

	return faceId
	conn.close()


def verify(personId):
	headers = {
    	'Content-Type': 'application/json',
    	'Ocp-Apim-Subscription-Key': '{subscription-key}',
		}

	faceId = detect() #calling the detect() function to return faceId of the webcam picture

	body = "{'faceId': '%s', 'personGroupId': '{personGroupId}', 'personId': '%s'}" % (faceId, personId[0])

	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn.request("POST", "/face/v1.0/verify?", body, headers)

	response = conn.getresponse()
	data = response.read()
	#transform response into json format
	data = json.loads(data)

	conn.close()
	# if confidence of analysis is more than 70%, return as true, otherwise, as false.
	if data["confidence"] >= 0.70:
		print("This is " + personId[1], data['confidence'])
	else:
		print("This is not " + personId[1], data['confidence'])
	


def draw():
	im = np.array(Image.open(FILENAME), dtype=np.uint8)

	#create figure and axes
	fig,ax = plt.subplots(1)

	#display the image
	ax.imshow(im)

	#create a rectangle patch for the face and then attach to axis
	rect = patches.Rectangle((targetFace[0],targetFace[1]),targetFace[2],targetFace[3],linewidth=2,edgecolor='r',facecolor='none')
	ax.add_patch(rect)

	#create circles patches for face landmarks and then attach each to axis
	for i in faceLandmarks:
		x, y = i['x'], i['y']
		circle = patches.Circle((x,y),5, color = 'r', fill = True)
		ax.add_patch(circle)

	#show image in window
	plt.show()


if __name__ == '__main__':
	get_ids(personId) #get all present ids from person group
	camstream() #take picture with camera to be analysed
	for i in personId: #for each personId, e.g. for each person in the person group, check confidence in
		verify(i) #detect() is called inside this function
	draw() #draw 27 points and rectangle on image taken by webcam