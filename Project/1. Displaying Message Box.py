import tkinter as tk
import tkinter.messagebox as msgbox

def showmsg():
    msgbox.showinfo("Title of the message", "Content of the message")
    #msgbox.showwarning("Title of the warning message", "Content of the warning message")
    #msgbox.showerror("Title of the error message", "Content of the error message")
    #msgbox.askquestion("Title of the Ask message", "Content of the Ask Message")
    #msgbox.askyesno("Title of ask yes no message", "Content of the ask yes no message")
    #msgbox.askyesnocancel("Title of ask yes no cancel message", "Content of the ask yes no cancel message")
    #msgbox.askokcancel("Title of ask ok cancel message","Content of the ask ok cancel message")
    #msgbox.askretrycancel("Title of ask retry cancel message","Content of the as retry cancel message")
    

window = tk.Tk()
window.title("Displaying Message Box")
window.geometry("500x500")

lbl = tk.Label(window, text="We can show a message box using command")
lbl.pack()
btn = tk.Button(window, text="Click Me",command = showmsg)
btn.pack()

window.mainloop()
