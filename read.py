#Reading Images & Video

import cv2 as cv
#Reading images
img=cv.imread('PHOTOS/cat_large.jpg') #this method basically takes in a path to an image and returns that image as a matrix of pixels. 

cv.imshow('Cat', img) #basically displays the image as a new window


#Reading videos
capture=cv.VideoCapture('VIDEOS/dog.mp4') #webcab reference is generally 0 if multiple digits themn multiple cameras connected to it

while True:
    isTrue, frame=capture.read() #we grab the video frame to frame
    cv.imshow('Video', frame)
    
    #way to stop the Do from playing indefinitely is by saying if CV dont wait

    if cv.waitKey(20) &0xFF==ord('d'): #if letter d is pressed it beaks the loop
        break

capture.release()
cv.destroyAllWindows()                            

cv.waitKey(0)#a keyboard binding function, waits for a specific delay or time in milliseconds for a key to be pressed.So if u pass zero
             # it basically waits for an infinite amount of time for a keyboard key to be pressed.
             #open cv doesnt have inbuilt functions to have far greater than ur computer screen
