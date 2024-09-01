#Thresholding/Binarizing Images
# a binary realisation of an image-in general we want to take an image and convert it to a binary image that is an image where pixels are 
# either 0 or black or 255 or white 
"""Eg would be be to take an image and take some particular value that we;re going to acll the threshholding
value and compare each pixel of the image to this thresh hold of value,If that pixel intensity<thresh hold value we set that pixel intensity to zero.
And if it is above th then we set it to 255 or white -We can create a binary image just from a regulat standalone image"""
import cv2 as cv

img=cv.imread('PHOTOS/cats.jpg')
cv.imshow('Cats',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Simple Thresholding
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
"""It looks at the img compare each pixel value to this threshhold value
essentially returns two things thresh-thresholded img of binarized img & threshold which is the same value u passed 150"""
cv.imshow('Simple Threshold',thresh)

threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse',thresh_inv)

#Adaptive Thresholding
#maually specify a specific threshold value-let the computer find the optimal threshold value by itself
#that refines it binarises over the img.so thats an essence the entire crux of adaptive threshholding
adaptive_thresh=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11,9) #kernel size-11,c value for tune our threshold
cv.imshow('Adaptive Thresholding',adaptive_thresh)


"""computes a mean over those neighbourhood pixels and findsthe optimal threshold val for that
specific part & slides up down right and every part of an image"""
""" THE more u subtract the mean the more u get the accuate the one"""
#computing optimal thresholded val on the basis of mean
cv.waitKey(0)
# use ADAPTIVE_THRESH_GAUSSIAN_C bcz of weight added to each pixel we get better img
