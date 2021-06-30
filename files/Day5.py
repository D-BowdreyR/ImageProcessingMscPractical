#Day 5 creating automatic image registration
#Daniel Bowdrey-Roberts

from os import listdir
from pydicom import dcmread
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import interpolation, rotate
from scipy import optimize

dcm_image1 = dcmread('../images/dcm/IMG-0004-00001.dcm')
dcm_image2 = dcmread('../images/dcm/IMG-0004-00002.dcm')
dcm_image3 = dcmread('../images/dcm/IMG-0004-00003.dcm')
dcm_image4 = dcmread('../images/dcm/IMG-0004-00004.dcm')

# Fix for missing or incorrect Photometric Interpretation tag
dcm_image1.PhotometricInterpretation = 'YBR_FULL'
dcm_image2.PhotometricInterpretation = 'YBR_FULL'
dcm_image3.PhotometricInterpretation = 'YBR_FULL'
dcm_image4.PhotometricInterpretation = 'YBR_FULL'


plt.imshow(dcm_image1.pixel_array, cmap='Greens_r')
plt.imshow(dcm_image2.pixel_array,alpha=0.3, cmap='Reds_r')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
floating = ax.imshow(dcm_image2.pixel_array, cmap='Reds_r')
ax.imshow(dcm_image1.pixel_array,alpha=0.5, cmap='Greens_r')
#removed plt.show here to make the plot at the end work

#def cost functions
def CstFuncSumSq(Image1, Image2):
    return np.mean((Image1 - Image2)**2)

# a function to shift the image given x and y coordinates
# and return cost
def shiftwithcost(list_xy_shifts):
    global floating
    shifted_image = interpolation.shift(dcm_image2.pixel_array, list_xy_shifts, mode='nearest')
    return CstFuncSumSq(dcm_image1.pixel_array,shifted_image)

#function to shift image given a tuple of x and y coordinates
def shiftImages(list_xy_shifts):
    global floating
    shifted_image = interpolation.shift(dcm_image2.pixel_array,list_xy_shifts, mode='nearest')
    floating.set_data(shifted_image)
    fig.canvas.draw()

print(dcm_image1.pixel_array.shape)

res = optimize.brute(shiftwithcost,((-50,50),(-50,50)),finish=optimize.fmin)
print(res)

shiftImages(res)
plt.show()
