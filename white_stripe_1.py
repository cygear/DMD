#Author: Johannes
#Creates a picture of the size 1024x768 pixels and pastes three black stripes into it


import os
from PIL import Image,ImageDraw

for i in range(0, 24):
    img = Image.open('white.png')
    for j in range(0, 3):
        img.paste('black', (i * 25 + j * 180, 0,110 + 180 *j + i * 25, 768))
    img.save(os.getcwd() + '/tripple_slits/tripple_slit_' + str(i) + '.png')

#TODO: Write a GUI to enter width, height and distance between stripes as well as the total amount of stripes.