# face-recognition-scienceFair
##  Scripts present in this repository
Source code for science fair project. These are the functions of each python (series 3.x) scripts: <br>
* `add_face.py`: Add faces to certain person, specified by *personId*
* `create_person.py`: Create person, user adds name for the person and scripts returns their Id (*personId*); <br>
* `detect_file.py`: Same as `detect_webcam.py`, but with input photo from folder in user's computer; <br>
* `detect_webcam.py`: With input photo taken by computer webcam, the script will verify similaries with each persons in person <br>group, returning if the face is someone in the group, together with the confidence; <br>
* `get_ids.py`: Retrieve from each person, present in person group, their respective personId. <br>


## How to execute each script

### **`create_person.py`**
**I)** From the main directory, execute in the terminal:<br>
`python create_person.py firstName LastName`<br>
* For example: <br>
`python create_person.py Family Dad` <br>

Returns personId<br>
`fc83229d-01ae-41de-897d-3ba879552101`
<hr>

### **`add_face.py`**
**I)** From main directory, execute in the terminal: <br>`python add_face.py personId number_of_files`
* For example: <br>`python add_face.py fc83229d-01ae-41de-897d-3ba879552101 2`<br>

**II)** After executing the script, you will be then prompted to write the locations of the files:<br>
`File: `<br>

* For example: (after executing the previous command): <br>
`File: PersonGroup/Family1-Dad/Family1-Dad1.jpg`<br>
`File: PersonGroup/Family1-Dad/Family1-Dad2.jpg`<br>

Returns persistedFaceId:<br>
`{'persistedFaceId': '5b80307d-e004-4d9d-b668-e4f1b0c36bec'}` <br>
`{'persistedFaceId': '81401400-a7e4-4536-a3db-f4d5603b0466'}` <br>

<hr>

### **`detect_file.py`**
**I)** From the main directory, execute in the terminal:<br>
`python detect_file.py file` <br>
* For example: <br>
`python detect_file.py PersonGroup/Family1-Dad/Family1-Dad3.jpg` <br>

Returns file plotted with 27 facial landmarks and face rectangle, together with confidence of <br>similarity from each person:<br>
<img src="https://github.com/danielSbastos/face-recognition-scienceFair/blob/master/PersonGroup/Family1-Dad/dad_points.png?raw=true" width="500"> <bt>
`This is Family Dad 0.8723`

<hr>

### **`detect_webcam.py`**
**I)** From main directory, execute in the terminal:<br>
`python detect_webcam.py`<br>
*Since I don't have "Family Dad" as a person by my side, I'm going to use an example of a webcam taking a <br> picture of my face, as seen on the gif below, and comparaing it to the people in my database*

Returns confidence of photo with each person in personGroup and photo with 27 face landmarks and face rectangle<br>
`This is not Anelise Bastos 0.0396`<br>
`This is not Isabela Bastos 0.18006`<br>
`This is Daniel Bastos 0.76689`<br>
<img src="https://github.com/danielSbastos/face-recognition-scienceFair/blob/master/PersonGroup/daniel.gif?raw=true" width="500"> <br>

<hr>

### **`get_ids.py`**
**I)** From main directory, execute in the terminal:<br>
`python get_ids.py`<br>

Returns all ids in personGroup with their respective person name:<br>
`['fc83229d-01ae-41de-897d-3ba879552101', 'Family Dad']`<br>
`['51d9d7fc-720c-4f65-8aec-8f1959adb39c', 'Family Mom']`<br>
`['62bc7875-343d-4f76-b80c-62691656a349', 'Family Daughter']`

