# Image Processing code
#Daniel Bowdrey-Roberts

#import all libaries/functions required
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

ct_image = misc.imread("/Users/daniel/coding-workspace/dicom/images/CT.jpg", flatten=True)
plt.hist(ct_image.flatten(),bins=256, color='red')
plt.show()

#function to dispay the image at different window
#levels
def windowLevel(image,levelwindow,colormap):
    level, window =  levelwindow
    vmx = level + (window/2.0)
    vmi = level - (window/2.0)
    plt.imshow(image,cmap=colormap,vmin=vmi,vmax=vmx)
    plt.show()

#windowLevel(ct_image,(50,100),"Greys_r")

ct_image_bone = (125,100)
ct_image_air = (25,50)

windowLevel(ct_image,ct_image_bone,"Greys_r")
windowLevel(ct_image,ct_image_air,"Greys_r")


















