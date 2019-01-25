#Day 5 creating automatic image registration

import pydicom
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from scipy import misc
from scipy.ndimage import interpolation, rotate

dcm_directory = "/Users/daniel/coding-workspace/dicom/images/dcm/"

dcm_image1 = pydicom.read_file(dcm_directory+"IMG-0004-00001.dcm").pixel_array 
dcm_image2 = pydicom.read_file(dcm_directory+"IMG-0004-00002.dcm").pixel_array 
dcm_image3 = pydicom.read_file(dcm_directory+"IMG-0004-00003.dcm").pixel_array
dcm_image4 = pydicom.read_file(dcm_directory+"IMG-0004-00004.dcm").pixel_array

plt.imshow(dcm_image1)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
floating = ax.imshow(dcm_image1, cmap='Reds_r')
ax.imshow(dcm_image2,alpha=0.5, cmap='Greens_r')

#def cost functions 
def CstFuncSumSq(Image1, Image2):
    return np.mean((image1-Image2)**2)


# a function to shift the image given x and y coordinates
def shiftImages(list_xy_shifts,imagetoshift):
    global floating
    shifted_image = interpolation.shift(imagetoshift, list_xy_shifts, mode='nearest')
    floating.set_data(shifted_image)
    fig.canvas.draw()

def AutoReg():


