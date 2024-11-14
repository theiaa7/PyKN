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
    stringlbl = tk.Label(window, text="This is a label "+ str(counterlbl))
    stringlbl.pack()

def editlabel():
    global stringlbl
    stringlbl.configure(text="Edited Label")

def delabel():
    global stringlbl
    stringlbl.destroy()

def addbutton():
    global counterbtn
    counterbtn += 1
    global stringbtn
    stringbtn = "button"+str(counterbtn)
    stringbtn = tk.Button(window, text="This is a button "+str(counterbtn), command=showmsg)
    stringbtn.pack()

def addbutton2():
    global counterbtn
    counterbtn += 1
    global stringbtn
    stringbtn = "button"+str(counterbtn)
    stringbtn = tk.Button(window, text="This is a button "+str(counterbtn), command=showyesnomsg)
    stringbtn.pack()

def delbtn():
    global stringbtn
    stringbtn.destroy()

def showmsg():
    msgbox.showinfo("Message", "You just pressed a button")

def showyesnomsg():
    msgbox.askyesno("Message", "Do you just pressed a button ?")

def showcredits():
    msgbox.showinfo("Credits", "Created by Koding Next")

window = tk.Tk()
window.title("Simple Program")
window.geometry("300x300")

menubar = tk.Menu(window)

lblmenu = tk.Menu(menubar, tearoff = 0)
lblmenu.add_command(label="Add Label", command = addlabel)
lblmenu.add_separator()
lblmenu.add_command(label="Edit Label", command = editlabel)
lblmenu.add_separator()
lblmenu.add_command(label="Delete Label", command = delabel)
menubar.add_cascade(label="Label", menu = lblmenu)

btnmenu = tk.Menu(menubar, tearoff = 0)
btnmenu.add_command(label="Add Button", command = addbutton)
btnmenu.add_separator()
btnmenu.add_command(label="Add Button 2", command = addbutton2)
btnmenu.add_separator()
btnmenu.add_command(label="Delete Button", command = delbtn)
menubar.add_cascade(label="Button", menu = btnmenu)

menubar.add_command(label = "Credits", command = showcredits)

window.config(menu = menubar)
window.mainloop()
