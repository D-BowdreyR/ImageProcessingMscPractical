#Day 5 creating automatic image registration
#Daniel Bowdrey-Roberts

from os import listdir
from pydicom import dcmread
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import interpolation, rotate
from scipy import optimize
import os
import platform

currentDir = os.getcwd()
# read in the images
dcm_image1 = dcmread(currentDir+'/images/dcm/IMG-0004-00001.dcm')
dcm_image2 = dcmread(currentDir+'/images/dcm/IMG-0004-00002.dcm')
dcm_image3 = dcmread(currentDir+'/images/dcm/IMG-0004-00003.dcm')
dcm_image4 = dcmread(currentDir+'/images/dcm/IMG-0004-00004.dcm')

# Fix for missing or incorrect Photometric Interpretation tag
dcm_image1.PhotometricInterpretation = 'YBR_FULL'
dcm_image2.PhotometricInterpretation = 'YBR_FULL'
dcm_image3.PhotometricInterpretation = 'YBR_FULL'
dcm_image4.PhotometricInterpretation = 'YBR_FULL'

# plot image 1 and 2 against each other
fig1 = plt.figure(num='All Dicom Images')
# plt.imshow(dcm_image1.pixel_array, cmap='Greens_r')
# plt.imshow(dcm_image2.pixel_array, alpha=0.3, cmap='Reds_r')
plt.imshow(dcm_image3.pixel_array, cmap='Blues_r')
plt.imshow(dcm_image4.pixel_array, alpha=0.3, cmap='Purples_r')
plt.show()

# create a new plot
fig2 = plt.figure(num="Image Registration")
ax = fig2.add_subplot(111)
ax.set_title('DICOM Images overlayed', fontsize=18, fontweight='bold')
ax.set_xlabel('X')
ax.set_ylabel('Y')
txt = "Move the overlayed image using the arrow keys on your keyboard.\n \
        To move quicker use the following key combinations \n \
        Mac: cmd+arrowKey, Win/Linux: ctrl+arrowKey. \n \
        Press the 'a' key to apply automated image registration"
plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)
# add the images to the plot
floating = ax.imshow(dcm_image2.pixel_array, cmap='Reds_r')
ax.imshow(dcm_image1.pixel_array, alpha=0.5, cmap='Greens_r')
currentpos = [0,0]

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

def getAutoRegisterImageShift():
    # result of optimised image registration
    return optimize.brute(shiftwithcost,((-50,50),(-50,50)),finish=optimize.fmin)

#function to shift image given a tuple of x and y coordinates
def shiftImages(list_xy_shifts):
    global floating
    shifted_image = interpolation.shift(dcm_image2.pixel_array,list_xy_shifts, mode='nearest')
    floating.set_data(shifted_image)
    fig2.canvas.draw()

def handleKeyPress(event):
    global currentpos
    minIncrement = 1
    maxIncrement = 10
    
    # handle key presses
    if event.key == "right":
        currentpos[1] += minIncrement
    elif event.key == getKeyForOS()+"+right":
        currentpos[1] += maxIncrement    
    elif event.key == "left":
        currentpos[1] -= minIncrement
    elif event.key == getKeyForOS()+"+left":
        currentpos[1] -= maxIncrement 
    elif event.key == "up":
        currentpos[0] -= minIncrement
    elif event.key == getKeyForOS()+"+up":
        currentpos[0] -= maxIncrement
    elif event.key == "down":
        currentpos[0] += minIncrement
    elif event.key == getKeyForOS()+"+down":
        currentpos[0] += maxIncrement
    elif event.key == "a":
        print(event.key)
        currentpos = getAutoRegisterImageShift()
    
    shiftImages([currentpos[0], currentpos[1]])

def getKeyForOS():
    if platform.system() == 'Darwin':
        return "cmd"
    else:
        return "ctrl"

fig2.canvas.mpl_connect('key_press_event',handleKeyPress)
plt.show()