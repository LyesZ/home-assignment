# Home assignment - Tomato allergies

Open domain image classification which is done with Tensorflow & Google colab developpement environnement.



## Dataset preprocessing 

The Preprocessing.py script prepares the database (assignement_imgs folder) to be included in the Tensorflow Object detection API.

The process description is included in the script.

Requirements to run it :

Pillow 2.2.1 : 

pip install Pillow==2.2.1


## Model training

This uses a modified version of the tutorial that you can find in this link (using Google Colab):

https://medium.com/swlh/how-to-train-an-object-detection-model-easy-for-free-f388ff3663e

The modified version is in this repository :

https://github.com/LyesZ/object_detection_demo
 

## Tomatos detector

The 'main.py' script exploits the frozen inference graph and the labelmap file stored in the 'model' folder to detect if there's tomatos in the images stored in the 'test' folder.
The script returns if there's tomatos or not (True / False) in the images that will be stored in the 'result_imgs' folder with bounding boxes (or not).

### Requirements to run 'main.py' :

Tensorflow V1.15.0 : 
			pip install tensorflow==1.15.0

Numpy : 
			pip install numpy

Six:
			pip install --user six

Matplotlib:
			pip install matplotlib

Pillow :
			pip install Pillow

The tensorflow object detection API :
			By following the instructions in this link : 
					https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md






