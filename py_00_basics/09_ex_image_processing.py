import matplotlib.pyplot as plt
import noise
import random
import math
from PIL import Image
import numpy as np


img = Image.open('data/crane.jpg')
rotated_image = img.rotate(180)
img = rotated_image
pixel_values = img.load()
def remap(value, low1, high1, low2, high2):
    
    return low2 + (value - low1) * (high2 - low2) / (high1 - low1)
    
#set size of figure
plt.figure(figsize=(10,10))

width = 50
height = 50

#set limits of axis
plt.xlim(0, 50)
plt.ylim(0, 50)

numx = 50
numy = 50

dx = float(width)/numx
dy = float(height)/numy

for y in range(numy):
    for x in range(numx):
        px = x*dx+dx/2
        py = y*dy+dy/2
        
        c = remap(px, 0, width, 0, img.width)
        r = remap(py, 0, height, 0, img.height)
        col = pixel_values[int(c),int(r)]
        
        my_color = [col[0]/255, col[1]/255, col[2]/255]
        cir = plt.Circle((px, py), dx/2, color = my_color)
        
        plt.gcf().gca().add_artist(cir)

plt.show()