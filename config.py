from tkinter import *
from tkinter import messagebox
import sys
import os
import cv2
import cap
from imutils import paths
import face_recognition
import argparse
import pickle

img_id = 1    
root = Tk()
content = Frame(root)
content.pack()
root.geometry("680x368")
root.title("เพิ่มฬบหน้าผู้ใช้")
root.option_add("*Font","consolas 20")
Name = StringVar()
Names = StringVar()

def message() :

    mess = messagebox.askyesno("Configtulation", "Do you want to config data?", icon='warning')
    if mess == 1 :
        l1 =Label(content, text="เพิ่มใบหน้าผู้ใช้").pack()
        E1 = Entry(content,textvariable=Name) . pack()
        b3 = Button(content,text ="MakeNewRoomer",command= PrintName) .pack()
        l3 = Label(content, text="ลบใบหน้าผู้ใช้").pack()
        E2 = Entry(content,textvariable=Names) . pack()
        b5 = Button(content,text= "Delete",command = Del) .pack()
        b6 = Button(content,text ="Close",command = root.destroy).pack()
        
    else : root.destroy()


    root.mainloop()



def PrintName() :  
    Names=Name.get()
    mlabel = Label(content,text=Names).pack()
    os.chdir("dataset")
    try:
        if not os.path.exists(Names):
            os.makedirs(Names)
    except OSError:
        print("ERROR : Can not make floder!!!")
    os.chdir("{}".format(Names)) 
    Locat = os.getcwd()
    print(Locat)
    cap.openCamera(img_id)
    os.chdir("/home/pi/Guitest/dataset")
    
#ENCODING
    # grab the paths to the input images in our dataset
    required=True
    detection_method = "hog"

    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images("dataset"))
    print (os.getcwd())

    # initialize the list of known encodings and known names
    knownEncodings = []
    knownNames = []

    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
	    # extract the person name from the image path
	    print("[INFO] processing image {}/{}".format(i + 1,
		    len(imagePaths)))
	    name = imagePath.split(os.path.sep)[-2]
	    print(imagePaths[i])
	    # load the input image and convert it from RGB (OpenCV ordering)
	    # to dlib ordering (RGB)
	    image = cv2.imread(imagePath)
	    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	    # detect the (x, y)-coordinates of the bounding boxes
	    # corresponding to each face in the input image
	    boxes = face_recognition.face_locations(rgb,
		    model=["detection_method"])

	    # compute the facial embedding for the face
	    encodings = face_recognition.face_encodings(rgb, boxes)

	    # loop over the encodings
	    for encoding in encodings:
		    # add each encoding + name to our set of known names and
		    # encodings
		    knownEncodings.append(encoding)
		    knownNames.append(name)

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("encodings.pickle", "wb+")
    f.write(pickle.dumps(data))
    print("Encoding Successful ")
    f.close()
    
def Del() :
    i = 1
    a = True

    Name = Names.get()
    os.chdir("/home/pi/Guitest/dataset/{}".format(Name))
    while(a) :
        b = str(i)
        os.remove("{}.jpg".format(b))
        i+= 1
        print("Remove img "+ b)
        if i == 20 :
            a=False
           
    os.chdir("/home/pi/Guitest/dataset/")
    os.rmdir("{}".format(Name))
    os.chdir("/home/pi/Guitest/")
    
    #ENCODING
    # grab the paths to the input images in our dataset
    required=True
    detection_method = "hog"

    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images("dataset"))
    print (os.getcwd())

    # initialize the list of known encodings and known names
    knownEncodings = []
    knownNames = []

    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
	    # extract the person name from the image path
	    print("[INFO] processing image {}/{}".format(i + 1,
		    len(imagePaths)))
	    name = imagePath.split(os.path.sep)[-2]
	    print(imagePaths[i])
	    # load the input image and convert it from RGB (OpenCV ordering)
	    # to dlib ordering (RGB)
	    image = cv2.imread(imagePath)
	    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	    # detect the (x, y)-coordinates of the bounding boxes
	    # corresponding to each face in the input image
	    boxes = face_recognition.face_locations(rgb,
		    model=["detection_method"])

	    # compute the facial embedding for the face
	    encodings = face_recognition.face_encodings(rgb, boxes)

	    # loop over the encodings
	    for encoding in encodings:
		    # add each encoding + name to our set of known names and
		    # encodings
		    knownEncodings.append(encoding)
		    knownNames.append(name)

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("encodings.pickle", "wb+")
    f.write(pickle.dumps(data))
    print("Encoding Successful ")
    f.close()
    
    os.chdir("/home/pi/Guitest/")
    messagebox.showinfo(title='Remove User',message="Remove Successed")
    return

def Exit() :
    root.destroy()
    
     
#Tk.KeyboardEntry(parent, keysize=5, keycolor='white').pack()


  
message()
    
