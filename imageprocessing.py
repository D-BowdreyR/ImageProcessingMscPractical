# Image Processing code
#Daniel Bowdrey-Roberts

#import all libaries/functions required
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

ct_image = misc.imread("images/CT.jpg", flatten=True)
plt.hist(ct_image.flatten(),bins=256, color='red')
plt.show()

#function to dispay the image at different window
#levels
def windowLevel(image,level,window,colormap):
    #calculate vmin and vmax from window and level
    vmx = level + (window)/2.0
    vmi = level - (window/2.0)
    plt.imshow(image,cmap=colormap,vmin=vmi,vmax=vmx)
    return plt.show()


windowLevel(ct_image,500,200,"Greys_r")






