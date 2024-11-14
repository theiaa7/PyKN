import tkinter as tk

window = tk.Tk()
window.title("Multiple Windows")
window.geometry("500x500")

lbl1 = tk.Label(window, text="This is the main window, this is the window open when the software start")
lbl1.pack()

extraWindow = tk.Toplevel(window)
extraWindow.title("I am the extra window")
extraWindow.geometry("500x500")
lbl2 = tk.Label(extraWindow, text = "This is an another window. Closing this window will not close the application")
lbl2.pack()

window.mainloop()
