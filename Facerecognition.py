import cv2
import os
from PIL import Image
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
name = "Face"
path = "dataset"
Name=""

def draw(img,classifier,scaleFactor,minNeighbors,color,clf,name) :
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features= classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords=[]
    for (x,y,w,h) in features :
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        id,_=clf.predict(gray[y:y+h,x:x+w])
        Name = os.path.split(image)[1].split(".")[1]
        print(Name)

        if id == 1:
            
            cv2.putText(img,Name,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1)
            
        coords=[x,y,w,h]
    return img,coords

def detect(img,faceCascade,img_id,clf):
    img,coords = draw (img,faceCascade,1.1,10,(255,0,0),clf,name)
    face_id = 1
    if len(coords)==4 :
        face_id = 1
        result = img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
        

    return img
    
        
        
img_id=0
cap = cv2.VideoCapture(0)
clf=cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.xml")
while (True) :
    ret,frame =cap.read()
    frame=detect(frame,faceCascade,img_id,clf)
    cv2.imshow('Cam1',frame)
    if cv2.waitKey(1) == 27 :
        break
cap.release()
cv2.destroyAllWindows()
    
