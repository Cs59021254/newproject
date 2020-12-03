import os 
from tkinter import *


i = 1
a = True
def de () :
    #name = Name.get()
    os.chdir("/Volumes/CEDA_X64FRE/Guitest/dataset/")
    #os.chdir('{}'.format(name))
    b = os.getcwd()
    print(b)
   # while(a) :
       # os.remove("{}.jpg".format(names))
       # i+= 1
       # if i == 20 :
       #     a=False
        #os.chdir("/Volumes/CEDA_X64FRE/Guitest/dataset/")
        #os.rmdir("{}".format(names))
        
        
root = Tk()
content = Frame(root)
content.pack()
root.geometry("680x368")
root.title("เพิ่มฬบหน้าผู้ใช้")
root.option_add("*Font","consolas 20")
Name = StringVar()
#l1 =Label(content, text="เพิ่มบหน้าผู้ใช้").pack()
#b1 =Button(content, text="Facerecoging",command=Face_rec) .pack()
#b2 =Button(content,text="Endcodeing",command=Encode).pack()
E1 = Entry(content,textvariable=Name) . pack()
#Names = Name.get()
#b3 = Button(content,text ="MakeNewRoomer",command= PrintName) .pack()

#b4 = Button(content,text= "capture")
#b4.pack()
#b4.bind('<Button-1>',capt)

b5 = Button(content,text= "Delete")
b5.pack()
b5.bind('<Button-1>',de)

root.mainloop()