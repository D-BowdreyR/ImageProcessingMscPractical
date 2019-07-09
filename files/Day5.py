#Day 5 creating automatic image registration
#Daniel Bowdrey-Roberts

from os import listdir
import pydicom
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import interpolation, rotate
from scipy import optimize

dcm_directory = "../images/dcm/"

dcm_image1 = pydicom.read_file(dcm_directory+"IMG-0004-00001.dcm").pixel_array 
dcm_image2 = pydicom.read_file(dcm_directory+"IMG-0004-00002.dcm").pixel_array 
dcm_image3 = pydicom.read_file(dcm_directory+"IMG-0004-00003.dcm").pixel_array
dcm_image4 = pydicom.read_file(dcm_directory+"IMG-0004-00004.dcm").pixel_array

plt.imshow(dcm_image1, cmap='Greens_r')
plt.imshow(dcm_image2, alpha=0.3, cmap='Reds_r')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
floating = ax.imshow(dcm_image2, cmap='Reds_r')
ax.imshow(dcm_image1,alpha=0.5, cmap='Greens_r')
#removed plt.show here to make the plot at the end work

#def cost functions
def CstFuncSumSq(Image1, Image2):
    return np.mean((Image1 - Image2)**2)
    
# a function to shift the image given x and y coordinates 
# and return cost
def shiftwithcost(list_xy_shifts):
    global floating
    shifted_image = interpolation.shift(dcm_image2, list_xy_shifts, mode='nearest')
    return CstFuncSumSq(dcm_image1,shifted_image)

#function to shift image given a tuple of x and y coordinates
def shiftImages(list_xy_shifts):
    global floating
    shifted_image = interpolation.shift(dcm_image2,list_xy_shifts, mode='nearest')
    floating.set_data(shifted_image)
    fig.canvas.draw()

print(dcm_image1.shape)

res = optimize.brute(shiftwithcost,((-50,50),(-50,50)),finish=optimize.fmin)
print(res)

shiftImages(res)
plt.show()