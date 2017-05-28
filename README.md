# face-recognition-scienceFair
### Microsoft Cognitive Face API will be used

Source code for science fair project. These are the functions of each python (series 3.x) scripts: <br>
* `add_face.py`: Add faces to certain person, specified by *personId*
* `create_person.py`: Create person, user adds name for the person and scripts returns their Id (*personId*); <br>
* `detect_one_file.py`: Same as `detect_webcam.py`, but with input photo from folder in user's computer; <br>
* `detect_webcam.py`: With input photo taken by computer webcam, the script will verify similaries with each persons in person <br>group, returning if the face is someone in the group, together with the confidence; <br>
* `get_ids.py`: Retrieve from each person, present in person group, their respective personId. <br>


### How to execute the scripts.
#### `add_faces.py`
From main directory, execute in terminal:<br>
`python add_face.py personId number_of_files`<br>
- For example: `python add_face.py fc83229d-01ae-41de-897d-3ba879552101 2`<br>
The script will then ask you to insert the same number of files as written on the command<br>
- For example: (after executing the previous command): <br>
`File: some/directory/with/image.png`
`File: some/directory/with/image2.png`



