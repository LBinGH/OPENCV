#Histogram Computation

"""Histogram allows u to visualize the distribution of pixel intensities in an image(rgb or gray scale img) so whether its a color image
or whether its a gray scale image u can visualize these pixel intensity distribution with this histogram
Compute a histogram for grayscale images and compute a histogram for RGB images"""
#helpful in computer vison projects
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('PHOTOS/cats.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask',masked)

""" #Grayscale histogram
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])  #this method compute the histogram for the image that we pass into
Now this images is a list so we need to passin a list of images.

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show() """

#No of bins across x axis basically represent the intervals of pixel intensities 

#To compute a color histogram

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)