#image processing part 2
#Daniel Bowdrey-Roberts

#import required libaries and functions
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import interpolation, rotate

lungs_image1 = misc.imread("/Users/daniel/coding-workspace/dicom/images/lungs.jpg")
lungs_image2 = misc.imread("/Users/daniel/coding-workspace/dicom/images/lungs2.jpg")

plt.imshow(lungs_image1)
plt.show()
plt.imshow(lungs_image2)
plt.show()
