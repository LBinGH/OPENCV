#Image Transformations

import cv2 as cv
import numpy as np

img=cv.imread('PHOTOS/park.jpg')

cv.imshow('Park',img)

#Translation-u can shift can shit img up ryt down
def translate(img, x,y):  
    #x & y basically stands for the number of pixels, u want to shift along the x and y axis respectively
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#-x negative x values --->shift left
#-y negative x values --->shift up
#+x positive x values --->shift right
#+y positive x values --->shift down

translated=translate(img,100,100)
cv.imshow('Translated',translated)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2) 
    
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-45)
cv.imshow('Rotated',rotated)

rotated_rotated=rotate(img,-90)
cv.imshow('Rotated Rotated',rotated_rotated)


#Resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping
flip=cv.flip(img,1)#0-flipping vertically 1-flipping horizontally
cv.imshow('Flip',flip)

#Cropping
cropped=img[200:400,300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)