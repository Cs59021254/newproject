import cv2
from tkinter import *
import os 
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
i=0

def Cap(img,img_id) : 
        cv2.imwrite(''+str(img_id)+".jpg",img) 
        print("Write img"+str(img_id))   

def draw(img,classifier,scaleFactor,minNeighbors,color) :
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features= classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords=[]
    for (x,y,w,h) in features :
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
    return img

def detect(img,faceCascade,img_id):
    img = draw (img,faceCascade,1.1,10,(255,0,0)) 
    Cap(img,img_id)
    
    return img  


img_id = 1 
def openCamera(img_id):
    cap = cv2.VideoCapture(0) 
    a = True
    while (a) :
        ret,frame = cap.read()
        frame = detect(frame,faceCascade,img_id)
        cv2.imshow('content',frame)
        img_id+=1   
        cv2.waitKey(1) 
        if img_id == 20 :
            a=False
    cap.release()             
    cv2.destroyAllWindows()
