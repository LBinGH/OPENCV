#Blurring Techniques

#how to smooth and blur an image using various blur techniques
#Gaussian Blur is one of the popular methods in Blurring
#By using blurring technique u can reduce the noise i mean by using smoothing
import cv2 as cv

img=cv.imread('PHOTOS/cats.jpg')
cv.imshow('Cats',img)

#Averaging
#will essentially compute the pixel intensity of the middle pixel of the true center as the avg of the surrounding pixel intensities
#so basically the middle pixel intensity is avg of surrounding pixel intensities

average=cv.blur(img, (7,7)) #(3,3)-kernel size
cv.imshow('Average Blur', average)

""" so the higher kernel size more the blur will be going in the img"""
#Gaussian Blur
#instead of computing the avg of all this running pixel intensity each running pixel is given a particular weight
# & essentially avg of the products of those weights gives u the value of the true center-we will get less blur as commpared to averaging method
#smwt blur bcz weight is added
gauss=cv.GaussianBlur(img, (7,7), 0) #0-the standard deviation in x direction
cv.imshow('Gaussian Blur',gauss)

#Median Blur
#same as averaging but difference is it find the median of the surrounding pixels
"""Blurring techniques tends to be more effective in reducing noise in an image as comapred to averaging"""
#it looks like smudging an img
median=cv.medianBlur(img,7)
cv.imshow('Median Blur',median)

#Bilateral Blurring
#most effective and a lot of used in advanced computer vison projects 
"""Traditional blurring blurs the img without checking the edges but thhis blurring have the abilting to retain the edges as well in the blurred img"""
""" swt looks like median blurring"""
bilateral=cv.bilateralFilter(img,5,35,25) #sigma color which there are more colors in the neighbourhood when the blur is computed, sigma space thing
cv.imshow('Bilateral',bilateral)
cv.waitKey(0)
"""A window drawn over a specific part of an image & smtg happen on the pixels in the window
that is kernel size so essentially blur is applied to the middle pixel as a results of the pixels around it~surrounding pixels
"""