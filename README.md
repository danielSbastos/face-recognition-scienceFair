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
`python detect_file.py personId file` <br>
* For example: <br>
`python detect_file.py fc83229d-01ae-41de-897d-3ba879552101 PersonGroup/Family1-Dad/Family1-Dad3.jpg` <br>
Return file plotted with 27 facial landmarks and face rectangle<br>
![man](danielSbastos/face-recognition-scienceFair/PersonGroup/Family1-Dad/dad_points.png "man")


