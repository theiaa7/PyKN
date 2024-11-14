import tkinter as tk
import tkinter.messagebox as msgbox

def version():
    msgbox.showinfo("Version", "Current Version : 0.0")

def comingsoon():
    msgbox.showinfo("Message", "Coming Soon")

def credit():
    msgbox.showinfo("Credits", "Thank StackOverFlow")

window = tk.Tk()
window.title("Creating a menubar with submenu")
window.geometry("300x300")

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)
filemenu.add_command(label="Command 1", command=comingsoon)
filemenu.add_separator()
filemenu.add_command(label="Command 2", command=comingsoon)
filemenu.add_separator()
filemenu.add_command(label="Command 3", command=comingsoon)
menubar.add_cascade(label="Category", menu = filemenu)

insertmenu = tk.Menu(menubar)
insertmenu.add_command(label="Image", command=comingsoon)
insertmenu.add_separator()
insertmenu.add_command(label="Chart", command=comingsoon)
insertmenu.add_separator()
insertmenu.add_command(label="Video", command=comingsoon)
menubar.add_cascade(label="Insert", menu = insertmenu)

#tearoff function is to make the menu non-detachable
helpmenu = tk.Menu(menubar, tearoff = 0)
#command can be added so when we choose a menu, it will do the assigned function
helpmenu.add_command(label="Version About", command=version)
helpmenu.add_separator()
helpmenu.add_command(label="Credit", command=credit)
menubar.add_cascade(label="Help", menu = helpmenu)

window.config(menu=menubar)
window.mainloop()
