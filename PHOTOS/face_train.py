import os
import cv2 as cv
import numpy as np

people=['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
DIR=r'C:\Users\Likhitha bhavana\Desktop\OPEN CV\FACES\train'


haar_cascade=cv.CascadeClassifier('haar_face.xml')

features=[] #arrays of imgs
labels=[] #whose img is it belongs to
def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for(x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
                #converting label to  numeric values to reduce the strain

create_train()
print('Training done------------')

#print(f'Length of the featues = {len(features)}')
#print(f'Length of the featues = {len(labels)}')

features=np.array(features,dtype='object')
labels=np.array(labels)
face_recognizer=cv.face.LBPHFaceRecognizer_create()

#Train the Recognizer on the feature list and the labels list

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)


#We can essentially create a function called def create unscrewed train that will essentially loop over every folder in this base folder.And inside that folder
#its going to loop over every image and essentially grab the face in that image and essentially add that to our training set.So our training set set will consist of two lives.
