import tkinter as tk
import tkinter.messagebox as msgbox

counterlbl = 0
stringlbl = ""
counterbtn = 0
stringbtn = ""

def addlabel():

    global counterlbl
    counterlbl += 1
    global stringlbl
    stringlbl = "label"+str(counterlbl)
    stringlbl = tk.Label(window, text="This is label "+ str(counterlbl))
    stringlbl.pack()

def editlabel():

    global stringlbl
    stringlbl.configure(text="Edited Label "+str(counterlbl))

def delabel():

    global stringlbl
    stringlbl.destroy()

def addbutton():
    
    global counterbtn
    counterbtn += 1
    global stringbtn
    stringbtn = "button"+str(counterbtn)
    stringbtn = tk.Button(window, text="This is button "+ str(counterbtn), command = showmsg)
    stringbtn.pack()

def editbtn():
    
    global stringbtn
    stringbtn.configure(text="Edited button "+str(counterbtn))

def delbtn():

    global stringbtn
    stringbtn.destroy()
    
def showmsg():
    msgbox.showinfo("Message","Testing a button")
    
window  = tk.Tk()
window.title("Functional Menubar")
window.geometry("500x500")

menubar = tk.Menu(window)

menubar.add_command(label="Add Label",command = addlabel)
menubar.add_command(label="Edit Label", command = editlabel)
menubar.add_command(label="Delete Label", command = delabel)
menubar.add_command(label="Add Button", command = addbutton)
menubar.add_command(label="Edit Button", command = editbtn)
menubar.add_command(label="Delete Button", command = delbtn)

window.config(menu = menubar)
window.mainloop()
