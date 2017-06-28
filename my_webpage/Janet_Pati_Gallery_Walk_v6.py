# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import PIL

import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations

backgroundColor = (0,)*3
pixelSize = 9

image = Image.open('ButterFly.jpg')  #this is resizing the image
image = image.resize((image.size[0]/pixelSize, image.size[1]/pixelSize), Image.NEAREST)
image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)
pixel = image.load()

for i in range(0,image.size[0],pixelSize):  #Change image to pixel image
    for j in range(0,image.size[1],pixelSize):
        for r in range(pixelSize):
            pixel[i+r,j] = backgroundColor
            pixel[i,j+r] = backgroundColor

image.save('pixelButterFly.png')

image = image.filter(ImageFilter.BLUR)
image.save('blurButterFly.png')

image = image.filter(ImageFilter.CONTOUR)
image.save('contourButterFly.png')

image=  Image.open('ButterFly.jpg')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('invertedButterFly.png')

'''Read the image data'''
   # Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
  # Build an absolute filename from directory + filename
filename = os.path.join(directory, 'ButterFly.jpg')
filename2 = os.path.join(directory, 'blurButterFly.png')
filename3 = os.path.join(directory, 'invertedButterFly.png')
filename4 = os.path.join(directory, 'contourButterFly.png')
filename5 = os.path.join(directory, 'pixelButterFly.png')

  # Read the image data into an array
img = plt.imread(filename)
img2 = plt.imread(filename2)
img3 = plt.imread(filename3)
img4 = plt.imread(filename4)
img5 = plt.imread(filename5)

'''Show the image data'''
  # Create figure with 1 subplot
fig, ax = plt.subplots(1, 5)
  # Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[0].axis('off')

ax[1].imshow(img2, interpolation='none')
ax[1].axis('off')
ax[2].imshow(img3, interpolation='none')
ax[2].axis('off')
ax[3].imshow(img4, interpolation='none')
ax[3].axis('off')
ax[4].imshow(img5, interpolation='none')
ax[4].axis('off')

  # Show the figure on the screen
fig.show()
