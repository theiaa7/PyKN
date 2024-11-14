import tkinter as tk

def showpopup():
    popup.deiconify()

def closepopup():
    popup.withdraw()

def destroypopup():
    popup.destroy()
    

window = tk.Tk()
window.title("Main Window")
window.geometry("500x500")

lbl1 = tk.Label(window, text="This is a main window")
lbl1.pack()

btn1 = tk.Button(window, text="Click me to show a pop-up window", command=showpopup)
btn1.pack()

popup = tk.Toplevel(window)
popup.title("Pop-up Window")
popup.geometry("300x300")

lbl2 = tk.Label(popup, text="You open a pop-up window")
lbl2.pack()
btn2 = tk.Button(popup,text="Click me to close", command = closepopup)
btn2.pack()
btn3 = tk.Button(popup, text="Click me to close and never can opened again", command = destroypopup)
btn3.pack()

popup.withdraw()
window.mainloop()
