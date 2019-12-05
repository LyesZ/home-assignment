#!usr/bin/python
# -*- coding: utf-8 -*-

'''This code takes the annotations json file and extracts all the coordinates of the bounding boxes that corresponds 
to the tag : tomates coupées that you can find in the label_mapping.csv file. Then it saves them into a new 
csv file (annotations.csv) and copies the corresponding images to the 'tomatos' folder'''

import json
import os
import csv
from shutil import copyfile
from PIL import Image 

tomates_entieres = "4e884654d97603dedb7e3bd8991335d0_lab"
tomates_cerises = "9f2c42629209f86b2d5fbe152eb54803_lab"
tomates_coupes =  "939030726152341c154ba28629341da6_lab" #we will train a DL model for this class (about 500 images)

#Extracting the json data
with open('img_annotations.json') as json_file:
    data = json.load(json_file)

#Creating and saving the new csv file
with open('anotations.csv', 'w+') as csvfile: 
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['filename','width','height','class','xmin','ymin','xmax','ymax'])

    for i in data.items():
        Filename = i [0]
        Annotations = i [1]
        for Label in Annotations:
            if Label.get("id") == tomates_coupes:
                copyfile(os.getcwd()+"/assignment_imgs/"+Filename, os.getcwd()+"/tomatos/"+Filename)
                bbox = Label.get("box")
                with Image.open(os.getcwd()+"/assignment_imgs/"+Filename) as img:
                    width, height = img.size
                #Writing the file (Image Name, Image Width, Image Height, Class Name, Xmin, Ymin, Xmax, Ymax)
                filewriter.writerow([Filename, width, height, "Tomates", bbox[0], bbox[1], bbox[0]+bbox[2], bbox[1]+bbox[3]])
csvfile.close()

''''This second part takes the newly created (csv) and copied (jpg & jpeg) files and separates them randomly with an arbitrary pourcentage
    that you can modify (default is set to 30% of the database for the test set and 70% for the training sets) '''

paths = os.listdir("tomatos")
separation = 0.3 #You can modify this pourcentage as you like but do it in a way that train dataset must contain most images
train = int(len(paths)-round(len(paths)*separation))  
# Annotations data extraction
with open('anotations.csv', newline='') as csvfile: 
    content = csv.reader(csvfile, delimiter=',')
    name= []
    width= []
    height= []
    clas= []
    xmin= []
    ymin= []
    xmax= []
    ymax = []
    for row in content:
        name.append(row[0])
        width.append(row[1])
        height.append(row[2])
        clas.append(row[3])
        xmin.append(row[4])
        ymin.append(row[5])
        xmax.append(row[6])
        ymax.append(row[7])
csvfile.close()

# The separation process into train & test then copying the corresponding files
with open('Database/train_labels.csv', 'w+') as csvfile: 
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['filename','width','height','class','xmin','ymin','xmax','ymax'])
    for i in range(train):
        copyfile(os.getcwd()+"/tomatos/"+paths[i], os.getcwd()+"/Database/train/"+paths[i])
        for j in range(len(name)):
            if paths[i] == name[j]:
                filewriter.writerow([paths[i],width[j],height[j],clas[j],xmin[j],ymin[j],xmax[j],ymax[j]])
csvfile.close()
    
with open('Database/test_labels.csv', 'w+') as csvfile: 
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['filename','width','height','class','xmin','ymin','xmax','ymax'])
    for i in range(train, len(paths)):
        copyfile(os.getcwd()+"/tomatos/"+paths[i], os.getcwd()+"/Database/test/"+paths[i])
        for j in range(len(name)):
            if paths[i] == name[j]:
                filewriter.writerow([paths[i],width[j],height[j],clas[j],xmin[j],ymin[j],xmax[j],ymax[j]])
csvfile.close()
