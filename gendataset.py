import cv2
import os
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
name = "pic."
Names = "tast"

def gen_dataset(img,face_id,img_id,Names) :
        
    cv2.imwrite(Names+str(face_id)+"."+str(img_id)+".jpg",img) 
    print("Write img"+str(img_id))       
    
    
    
def draw(img,classifier,scaleFactor,minNeighbors,color,text) :
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features= classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords=[]
    for (x,y,w,h) in features :
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1)
        coords=[x,y,w,h]
    return img,coords

def detect(img,faceCascade,img_id):
    img,coords = draw (img,faceCascade,1.1,10,(255,0,0),name)
    face_id = 1
    if len(coords)==4 :
        face_id = 1
        result = img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
        gen_dataset(result,face_id,img_id,Names)

    return img

    
    gen_dataset(img,face_id,img_id)
    return img  
    
        
        
img_id = 0
cap = cv2.VideoCapture(0)

while (True) :
    ret,frame =cap.read()
    os.chdir("/home/pi/NewProject/dataset")
    frame=detect(frame,faceCascade,img_id)
    cv2.imshow('Cam1',frame)
    img_id+=1
    if cv2.waitKey(1) == 27 :
        break
cap.release()
cv2.destroyAllWindows()
    
