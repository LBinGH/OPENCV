#Edge Detection

import cv2 as cv
import numpy as np

img=cv.imread('PHOTOS/park.jpg')
cv.imshow('Park',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Laplacian-left lacing edges
#this method computes the gradients of this image the grayscale image
lap=cv.Laplacian(gray, cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)
#IT looks like drwan with a chalkpiece

"""Image s cant have negative pixel images,so all the pixel values of img are converted to absolute values
then we convert it into ii 28 to an img specific dataype"""

#Sobel gradient Magnitude Represntation
"""Sobel computes the gradients in two directions the x and the y"""
sobelx=cv.Sobel(gray, cv.CV_64F,1,0)
sobely=cv.Sobel(gray, cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel',combined_sobel)

#canny is basically more advanced algo that actually uses sobel in one of its stages
#that actually uses sobel in one of it stages canny is multi stage process its a method to compute the gradients of the img
canny=cv.Canny(gray, 150, 175)
cv.imshow('Canny',canny)
cv.waitKey(0)
