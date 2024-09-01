#Color Channels

#How to split and merge color channels in open cv
"""a color image basically consists of multiple channels red,green and blue
u can take bgr img & split it into blue green and red components"""

import cv2 as cv
import numpy as np #a blank img using numpy

img=cv.imread('PHOTOS/park.jpg')
cv.imshow('Park',img)

blank=np.zeros(img.shape[:2], dtype='uint8')


b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank]) #red and green componets setting to blank
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)

merged=cv.merge([b,g,r])
cv.imshow('Merged Image',merged)


cv.waitKey(0)

#grayscale images have a shape of one

