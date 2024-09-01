#Essential Functions in OpenCV

import cv2 as cv

img=cv.imread('PHOTOS/park.jpg')
cv.imshow('park',img)

#Converting BGR images to gray scale so that u can see only the intensity distrivution of pixels
#rather than the color itself

#Converting to grayscale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur=cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT) #kernel size number should be odd
cv.imshow('Blur',blur)
#cv.waitKey(0)

#How to create an Edge Cascade
#we use canny edge detector bluuring+computational stuff

canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

#How to dilate an image using a specific structuring element-Dialating the Image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

#Eroding
eroded=cv.erode(dilated,(7,7),iterations=3) #to get back the original one i mean u get edge cascade
cv.imshow('Eroded',eroded)

#Resize
resized=cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)#intercubic is slower but gives high quality img than linear
cv.imshow('Resized',resized)

#Cropping
cropped=img[50:200,200:400] #array slicing
cv.imshow('Cropped',cropped)

cv.waitKey(0)
              
            