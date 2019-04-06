# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 20:16:27 2018

@author: tom
"""
"""Download images using google_images_download module
https://github.com/hardikvasa/google-images-download"""

from google_images_download import google_images_download

from PIL import Image

import glob, os

outdir = r'C:\Users\tom\Documents\Data Science MSc\Machine Learning\Assignment 2'

chrome = r'C:\Users\tom\chromedriver.exe'

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"formula 1 race action photo","limit":300,"print_urls":True, "format":"jpg","chromedriver":chrome,
             "output_directory":outdir, "size":">400*300"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths) 


"""reduce all downloaded images to max pixel width of 300, with height adjusted to match
original height-width ratio"""

images = glob.glob(os.path.join(outdir, "formula 1 race action photo", "*.jpg"))

for i in images:
    try:
        img = Image.open(i)
        widthpercent = (300/float(img.size[0]))
        height = int((float(img.size[1])*float(widthpercent)))
        img = img.resize((300,height), Image.ANTIALIAS)
        img.save(i)
    except:
        print("problem with "+i.split('\\')[-1])