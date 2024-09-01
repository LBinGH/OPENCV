import cv2 as cv

img=cv.imread('PHOTOS/group 1.jpg')
cv.imshow('Group of 5 people',img)

#convert thsi img to grayscale img
#face dtection doesnt involve skin tone or the colrs that are presnt in the image
#THESE HAARCASCADES cessentially look at an object in an img & using th edges tries to detremine whether its a face or not. 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')
#this one reads those 33,000 lines of xml code and store it in a variable called haar_cascade 

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
#essentially the rectangular coordinates of that face as a list to faces on the score rec.
#thats exactly why we are giving it faces on scope rect to rectangle.
print(f'Number of faces found= {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces',img)
cv.waitKey(0)

"""NOTE: We can essentially loop over the list and grab the corrdinates of those images and draw a rectangular over
the detected faces . HaarCascades are really sensitive to noise in an image. By tweakinng these vale min neighbours we can get better result.
Open CV has predefined classifiers"""