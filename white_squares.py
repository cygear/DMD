# Author: Johannes
# Creates a picture of the size 1024x768 pixels and pastes three black stripes into it


import os
from PIL import Image, ImageDraw

square = []
distance = [1, 5, 10, 15, 20]
for i in range(25):
    square.append(5 + i * 5)
for i in range(len(distance)):
    os.makedirs(os.getcwd() + '/white_squares/distance_' + str(distance[i]))
for i in range(len(distance)):
    for j in range(len(square)):
        # TODO: Figure out how to create convoluted directories in python with for loop
        # os.makedirs('/home/johannes/PycharmProjects/Educational/white_squares/distance_'+ str(distance[i]) + '/square_' + str(square[i]) + '_' + str(square[i]))
        for k in range(0, 50):
            img = Image.open('black.png')
            img.paste('white', (500 - square[j] - k * distance[i], 400, 500 - k * distance[i], 410))
            img.paste('white', (500 + k * distance[i], 400, 500 + square[j] + k * distance[i], 410))
            img.save(os.getcwd() + '/white_squares/distance_' + str(distance[i]) + '/square_' + str(square[i]) + '_' + str(square[i]) + str(k * 1) + '.png')