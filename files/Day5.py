#Day 5 creating automatic image registration

import pydicom
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from scipy import misc
from scipy.ndimage import interpolation, rotate
from scipy.optimize import brute

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
plt.show()

#function to shift image given a tuple of x and y coordinates
def shiftImages(list_xy_shifts):
    global floating
    shifted_image = interpolation.shift(dcm_image2,list_xy_shifts, mode='nearest')
    floating.set_data(shifted_image)
    fig.canvas.draw()

#def cost functions 
def CstFuncSumSq(Image1, Image2):
    return np.mean((Image1-Image2)**2)
    
# a function to shift the image given x and y coordinates 
# and return cost
def shiftwithcost(list_xy_shifts):
    global floating
    global dcm_image1
    global dcm_image2
    shifted_image = interpolation.shift(dcm_image2, list_xy_shifts, mode='nearest')
    floating.set_data(shifted_image)
    return CstFuncSumSq(dcm_image1,shifted_image)

print(dcm_image1.shape)

res = brute(shiftwithcost,((-50,50),(-50,50)))

shiftImages(res)
plt.show()