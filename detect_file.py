#libraries to plot face features
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

#libraries for apiconnection
import requests
import json
import sys

#Libraries to take photo with webcam
import pygame
import pygame.camera
from pygame.locals import *

''' INSERT FILE AND COMPARE IT WITH GROUP PERSON TO FIND SIMILAR PERSON '''

#info to save webcam photo
global FILENAME
FILENAME = sys.argv[1] #file insered by user will be be used for analysis

key = '{Ocp-Apim-Subscription-Key}' #YOUR key. Not gonna give you mine, smartypants

targetFace = []
faceLandmarks = []
personId = []

'''get all personIds in certain personGroup'''
def get_ids(personId, key):
  headers = {'Ocp-Apim-Subscription-Key': key}
  params = {'top': '100'}

  resp_get_ids = requests.get("https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/people/{personGroupId}?",
                              params = params,
                              headers = headers)

  data = json.loads(resp_get_ids.text)

  for i in range(len(data)):
    #append to list the person id with its correspondant name, e.g. [124534nbh424523n5, Gabriel]
    personId.append([data[i]["personId"],data[i]["name"]])


'''for the file, detect face coordinates and face landmarks, respectively appending them to targetFace and faceLandmarks'''
def detect(key, targetFace, faceLandmarks):
  headers_octet = {
      'Content-Type': 'application/octet-stream',
      'Ocp-Apim-Subscription-Key': key}

  params = {'returnFaceId': 'true', #return faceId and face coordinates
            'returnFaceLandmarks' : 'true'} #return 27 coordinates of face landmarks

  resp_detect = requests.post("https://westus.api.cognitive.microsoft.com/face/v1.0/detect?%",
                              params = params,
                              data = open(FILENAME, 'rb'),
                              headers = headers_octet)

  data = json.loads(resp_detect.text)
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


'''with photo already taken and having defined faceLandmarks and targetFace, check the confidence if it is
each person in personGroup'''
def verify(personId, key):
  headers_json = {'Content-Type': 'application/json',
              'Ocp-Apim-Subscription-Key': key}

  faceId = detect(key, targetFace, faceLandmarks) #calling the detect() function to return faceId of the webcam picture
  body = "{'faceId': '%s', 'personGroupId': 'people', 'personId': '%s'}" % (faceId, personId[0])

  resp_verify = requests.post('https://westus.api.cognitive.microsoft.com/face/v1.0/verify?',
                              data = body,
                              headers = headers_json)

  #with response, transform it to json and verify the confidence between each person in personGroup
  data = json.loads(resp_verify.text)
  if data["confidence"] >= 0.70: #if higher or equal than 70% of accuracy -> it is that person
    print("This is " + personId[1], data['confidence'])
  else: #if less than 70% of accuracy -> it is not that person
    print("This is not " + personId[1], data['confidence'])


''' plot the coordinates defined in faceLandmarks as circles and targetFace as rectangle in taken photo'''
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
  get_ids(personId,key) #get all present ids from person group
  camstream() #take picture with camera to be analysed
  for i in personId: #for each personId, e.g. for each person in the person group, check confidence in
    verify(i, key) #detect() is called inside this function
  draw() #draw 27 points and rectangle on image taken by webcam

