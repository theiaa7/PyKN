import tkinter as tk
import tkinter.messagebox as msgbox

def showmsg():
    result = msgbox.askyesno("Title of the message","Content of the message")
    if result == True:
        print("You press yes")
    elif result == False:
        print("You press no")

window = tk.Tk()
window.title("test")
window.geometry("300x300")

btn = tk.Button(window, text="Click Me", command=showmsg)
btn.pack()

window.mainloop()
