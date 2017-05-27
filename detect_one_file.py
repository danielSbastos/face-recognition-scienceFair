#libraries for api connection
import requests
import json

#libraries to plot face features
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

''' OPEN PHOTO AND COMPARE WITH GROUP PERSON TO FIND SIMILAR PERSON '''

global FILENAME
FILENAME = '{FILENAME}'

key = '{Ocp-Apim-Subscription-Key}' #YOUR key. Not gonna give you mine, smartypants
targetFace = []
faceLandmarks = []

def detect(key, targetFace, faceLandmarks):
  #api connection with microsoft server
  headers_octet = {
      'Content-Type': 'application/octet-stream',
      'Ocp-Apim-Subscription-Key': key}

  params = {'returnFaceId': 'true',
            'returnFaceLandmarks' : 'true'}

  resp_detect = requests.post("https://westus.api.cognitive.microsoft.com/face/v1.0/detect?%",
                              params = params,
                              data = open(FILENAME, 'rb'),
                              headers = headers_octet)
  #transform response into json
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
	detect(key, targetFace, faceLandmarks)
	draw()
