# Image Processing code
#Daniel Bowdrey-Roberts

#import all libaries/functions required
import numpy as np
import matplotlib.pyplot as plt
from  scipy import misc

ct_image = misc.imread("images/CT.jpg", flatten=True)
plt.hist(ct_image.flatten(),bins=256, color='red')
plt.show()





