# Resizing and Rescaling Frames

#Rescaling and Resizing-of files and images to prevent computational strain
#rescaling video implies modifying its height and width to a particular height & width
import cv2 as cv

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame, scale=0.75):
    #Images, Videos and Live Videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


resized_image=rescaleFrame(img)
cv.imshow('Image', resized_image)


def changeRes(width,height):  #changing the esolution of the image or the video
    #Only works for Live Videos
    capture.set(3,width)
    capture.set(4,height)

#Reading videos
capture=cv.VideoCapture('VIDEOS/dog.mp4') #webcab reference is generally 0 if multiple digits themn multiple cameras connected to it

while True:
    isTrue, frame=capture.read() #we grab the video frame to frame

    frame_resized=rescaleFrame(frame,scale=.2)


    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    #way to stop the Do from playing indefinitely is by saying if CV dont wait

    if cv.waitKey(20) &0xFF==ord('d'): #if letter d is pressed it beaks the loop
        break

capture.release()
cv.destroyAllWindows()                            

cv.waitKey(0)#a keyboard binding function, waits for a specific delay or time in milliseconds for a key to be pressed.So if u pass zero
             # it basically waits for an infinite amount of time for a keyboard key to be pressed.
             #open cv doesnt have inbuilt functions to have far greater than ur computer screen
