# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 10:34:08 2018

@author: tom
"""

import os, random

os.chdir(r'C:\Users\tom\Documents\Data Science MSc\Machine Learning\Assignment 2\formula 1 race action photo')

"""Rename images from 1 to n)"""
i = 1
    
for filename in os.listdir("."):
    ext = filename[-4:]
    new = "f1car_"+str(i) + ext
    os.rename(filename, new)
    i +=1

"""split files into folders for training, validation, test"""
    
files = [f for f in os.listdir(".") if f.endswith(".jpg")]

traininglen = 160
os.mkdir("training")
for i in range(0, traininglen):
    f = random.choice(files)
    files.remove(f)
    os.rename(f, os.path.join(os.getcwd(),"training",f))
    
validationlen = 40
os.mkdir("validation")
for i in range(0, validationlen):
    f = random.choice(files)
    files.remove(f)
    os.rename(f, os.path.join(os.getcwd(),"validation",f))
    
os.mkdir("test")
for f in files:
    os.rename(f, os.path.join(os.getcwd(),"test",f))


"""remove any that could not be labelled"""
    
xml_files = [f[:-4] for f in os.listdir(".") if f[-4:]=='.xml']

for filename in os.listdir("."):
    if filename[:-4] not in xml_files:
        os.remove(filename)