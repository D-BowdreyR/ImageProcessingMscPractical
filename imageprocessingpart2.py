#image processing part 2
#Daniel Bowdrey-Roberts

#import required libaries and functions
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import interpolation, rotate

lungs_image1 = misc.imread("/Users/daniel/coding-workspace/dicom/images/lungs.jpg")
lungs_image2 = misc.imread("/Users/daniel/coding-workspace/dicom/images/lungs2.jpg")

#show each image on seperate plots
plt.imshow(lungs_image1)
plt.show()
plt.imshow(lungs_image2)
plt.show()

#show both images on the same plot using transparency
plt.imshow(lungs_image1)
plt.imshow(lungs_image2, alpha=0.3)
plt.show()
