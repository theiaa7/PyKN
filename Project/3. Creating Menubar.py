import tkinter as tk

window = tk.Tk()
window.title("Creating a menubar")
window.geometry("500x500")

menubar = tk.Menu(window)

menubar.add_command(label="Menu 1")
menubar.add_command(label="Menu 2")
menubar.add_command(label="Menu 3")
                    
window.config(menu = menubar)
window.mainloop()
