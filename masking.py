#Masking

#using bitwise operators we can perform masking in open cv making essentially allows us to focus on certain parts of an
#image that we'd like to focus on

""" if u are interested in focusing on the faces of those ppl u could essentially apply masking 
& essentially mask over all the ppls faces and remove all the unwanted parts of the img- a high level intuition"""
import cv2 as cv
import numpy as np

img=cv.imread('PHOTOS/cats 2.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape[:2],dtype='uint8') #the dimmensions of the mask is same size as that of img // -100 pixels
cv.imshow('Blank Image',blank)

circle=cv.circle(blank.copy(),(img.shape[1]//2+45,img.shape[0]//2),100,255,-1)
#cv.imshow('Mask',mask)

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

weird_shape=cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape',weird_shape)

#Creating a masked image
masked=cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image',masked)
cv.waitKey(0)