import cv2
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import os
from os import listdir
from os.path import isfile, join
from imutils.video import VideoStream
from tkinter import *

def PrintName() :  
    Names=Name.get()
    mlabel = Label(content,text=Names).pack()
    os.chdir("dataset")
    try:
        if not os.path.exists(Names):
            os.makedirs(Names)
    except OSError:
        print("ERROR : Can not make floder!!!")
    return 

root = Tk()
content = Frame(root)
content.pack()
root.geometry("680x368")
root.title("เพิ่มฬบหน้าผู้ใช้")
root.option_add("*Font","consolas 20")
Name = StringVar()
l1 =Label(content, text="เพิ่มบหน้าผู้ใช้").pack()
b1 =Button(content, text="เริ่มถ่ายรูป",command=Face_rec) .pack()
E1 = Entry(content,textvariable=Name) . pack()
b3 = Button(content,text ="Print",command= PrintName) .pack()
RoomerName = Name.get()

i = 1
camera = PiCamera()
camera.crop = (0.22, 0.10, 0.40, 0.40)
camera.rotation = 0
camera.hflip = 1
camera.resolution = (368,288)
camera.framerate = 30
camera.brightness = 65
camera.brightness = 60

root = Tk()
content = Frame(root)
content.pack()
root.geometry("680x368")
root.title("เพิ่มฬบหน้าผู้ใช้")
root.option_add("*Font","consolas 20")
Name = StringVar()





root.mainloop()