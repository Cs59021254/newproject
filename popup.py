from tkinter import *
from tkinter import messagebox

top = Tk()
def deleteme():
    mess = messagebox.askyesno("Configtulation", "Do you want to config data?", icon='warning')
    if mess == 1 :
        import config
    else : top.destroy()

    
b1 = Button(top,text ="Exit")
b1.bind('<Button-1>',top.destroy())
b1.pack()
top.mainloop()


