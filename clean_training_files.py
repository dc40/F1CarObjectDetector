# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 10:34:08 2018

@author: tom
"""

import os

os.chdir(r'C:\Users\tom\Documents\Data Science MSc\Machine Learning\Assignment 2\formula one racing')

i = 1
    
for filename in os.listdir("."):
    ext = filename[-4:]
    new = "f1_"+str(i) + ext
    os.rename(filename, new)