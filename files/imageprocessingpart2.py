#image processing part 2
#Daniel Bowdrey-Roberts

#import required libaries and functions
import numpy as np
import matplotlib.pyplot as plt
import imageio
from scipy.ndimage import interpolation, rotate
import os

currentDir = os.getcwd()

lungs_image1 = imageio.imread(currentDir+"/images/lungs.jpg",as_gray=True)
lungs_image2 = imageio.imread(currentDir+"/images/lungs2.jpg", as_gray=True)
lungs_image3 = imageio.imread(currentDir+"/images/lungs3.jpg", as_gray=True)


#show each image on seperate plots
plt.imshow(lungs_image1)
plt.show()
plt.imshow(lungs_image2)
plt.show()
plt.imshow(lungs_image3)
plt.show()

#show both images on the same plot using transparency
plt.imshow(lungs_image1)
plt.imshow(lungs_image3, alpha=0.3)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
floating = ax.imshow(lungs_image3, cmap='RdPu')
ax.imshow(lungs_image1,alpha=0.5, cmap='YlGn')

# a function to shift the image given x and y coordinates
def shiftImages(list_xy_shifts, rotation_angle):
    global floating
    shifted_image = interpolation.shift(rotate(lungs_image3,rotation_angle), list_xy_shifts, mode='nearest')
    floating.set_data(shifted_image)
    fig.canvas.draw()

shiftImages([-25,-55], -5)
plt.show()

