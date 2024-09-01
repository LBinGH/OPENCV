#Color spaces

#color spaces is basically a space of colrs representing an array of pixel colors

import cv2 as cv
import matplotlib.pyplot as plt 
#u can see inversion of colors

img=cv.imread('PHOTOS/park.jpg')
cv.imshow('Park',img)

plt.imshow(img)
plt.show()

#BGR to Grayscale
"""gray scale images basically show u the sidtribution of pixel
intensities at particular locations of ur image"""
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV(Saturation value)
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()

#HSV to BGR
lab_bgr=cv.cvtColor(hsv,cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

#plt.imshow(rgb)
#plt.show()


cv.waitKey(0)


"""You cannot convert Grayscale image to HSV directly
grayscale to BGR then to HSV"""