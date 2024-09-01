#Contour Detection

#contours are useful tools when u get into shape analysis and object detection

import cv2 as cv
import numpy as np

img= cv.imread('PHOTOS/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges',canny)

#instead of using canny u can use threshhold function in opencv

#ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
#cv.imshow('Thresh',thresh)
#threshhold generally looks at an image and binarize that image
"""if a particular pixel is below 125 if the density of that pixel is below
125 its going to be set zero or blank if it is above 125 it is set to white or two by five """



contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#contours which is essentially a python list of all the coordinates of the contours that were found in the image
#hierarchies which is hierarchichial representation of contours

#contour approximation method-basically how we want to approximate the contour

print(f'{len(contours)} contour(s) found!')


cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)
cv.waitKey(0)

#note: dont do thresh hold 1st!! 1st do canning then do contour