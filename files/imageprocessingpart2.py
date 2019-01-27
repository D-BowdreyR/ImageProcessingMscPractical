#image processing part 2
#Daniel Bowdrey-Roberts

#import required libaries and functions
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import interpolation, rotate

lungs_image1 = misc.imread("/Users/daniel/coding-workspace/dicom/images/lungs.jpg",flatten=True)
lungs_image2 = misc.imread("/Users/daniel/coding-workspace/dicom/images/lungs2.jpg",flatten=True)

#show each image on seperate plots
plt.imshow(lungs_image1)
plt.show()
plt.imshow(lungs_image2)
plt.show()

#show both images on the same plot using transparency
plt.imshow(lungs_image1)
plt.imshow(lungs_image2, alpha=0.3)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
floating = ax.imshow(lungs_image2, cmap='RdPu')
ax.imshow(lungs_image1,alpha=0.5, cmap='YlGn')

# a function to shift the image given x and y coordinates
def shiftImages(list_xy_shifts):
    global floating
    shifted_image = interpolation.shift(lungs_image2, list_xy_shifts, mode='nearest')
    floating.set_data(shifted_image)
    fig.canvas.draw()

shiftImages([-25,-55])
plt.show()
