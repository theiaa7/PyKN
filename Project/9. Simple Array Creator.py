import tkinter as tk
import tkinter.ttk as combobox
import tkinter.messagebox as msgbox


def showpopup():
    popup = tk.Toplevel(window)
    popup.title("Example of popup")
    popup.geometry("300x300")

def inputdata():
    if inptname.get() != "" and inptstock.get() != "" and inptmanuf.get() != "" and inptware.get() != "":
        itemlist.append(inptname.get())
        stocklist.append(inptstock.get())
        manufacturerlist.append(inptmanuf.get())
        warehouselist.append(inptware.get())
        inptname.delete(0, tk.END)
        inptstock.delete(0, tk.END)
        inptmanuf.delete(0, tk.END)
        inptware.set(" ")
        #print(itemlist + stocklist + manufacturerlist + warehouselist)
    else:
        msgbox.showwarning("Warning", "Every Field should be filled to input data")

def viewlist():
    listwindow = tk.Toplevel(window)
    listwindow.title("Content of List")
    listwindow.geometry("300x400")
    itemheader = tk.Label(listwindow, text = "ITEM")
    stockheader = tk.Label(listwindow, text = "STOCK")
    manufacturerheader = tk.Label(listwindow, text = "MANUFACTURER")
    warehouseheader = tk.Label(listwindow, text="WAREHOUSE")
    itemheader.grid(column = 0, row =0)
    stockheader.grid(column = 1, row =0)
    manufacturerheader.grid(column = 2, row =0)
    warehouseheader.grid(column = 3, row =0)
    for i in range(0, len(itemlist)):
        itemlabel = tk.Label(listwindow, text = itemlist[i])
        stocklabel = tk.Label(listwindow, text = stocklist[i])
        manufacturerlabel = tk.Label(listwindow, text = manufacturerlist[i])
        warehouselabel = tk.Label(listwindow, text = warehouselist[i])
        itemlabel.grid(column = 0, row = i+ 1)
        stocklabel.grid(column = 1, row = i+1)
        manufacturerlabel.grid(column = 2, row = i+1)
        warehouselabel.grid(column = 3, row = i+1)
        #print(itemlist[i] + stocklist[i] + manufacturerlist[i] + warehouselist[i])

def clearlist():
    if len(itemlist) != 0:
        choice = msgbox.askyesno("Warning","You are going to delete the content of your list, proceed ?")
        if choice == True:
            itemlist.clear()
            stocklist.clear()
            manufacturerlist.clear()
            warehouselist.clear()
            msgbox.showinfo("Notice","Your List is now empty")
    else:
        msgbox.showinfo("Notice", "Your List is already empty")


def credit():
    creditwin = tk.Toplevel(window)
    creditwin.title("Credits")
    creditwin.geometry("500x100")
    label = tk.Label(creditwin, text="This software is done because the help of stackoverflow and google")
    label2 = tk.Label(creditwin, text="Also thankful to all online reference and documentation of the library")
    label.pack()
    label2.pack()

def version():
    verwin = tk.Toplevel(window)
    verwin.title("Version")
    verwin.geometry("200x100")
    label = tk.Label(verwin, text="Current software version : 1.00")
    label.pack()
        
itemlist = []
stocklist = []
manufacturerlist = []
warehouselist = []
    
window = tk.Tk()
window.title("Simple Array Creator")
window.geometry("500x300")

lbltitle = tk.Label(window, text="Welcome to Warehouse Program")
lbldesc = tk.Label(window, text="With this program, we can store inputted data from the user to array which later can be viewed.")

lblname = tk.Label(window, text="Item name: ")
lblstock = tk.Label(window, text="Stock: ")
lblmanuf = tk.Label(window, text="Manufacturer: ")
lblware = tk.Label(window, text="Warehouse: ")
inptname = tk.Entry(window, width = 20)
inptstock = tk.Entry(window, width = 20)
inptmanuf = tk.Entry(window, width = 20)
inptware = combobox.Combobox(window,width = 20, values=("Jakarta","Tangerang","Bekasi"), state = "readonly")
inptware.bind("<<ComboboxSelected>>", lambda x : lbltitle.focus())
inptbtn = tk.Button(window, text="Input Data", command = inputdata)

lbltitle.grid(row = 0, column = 0, columnspan = 2, sticky = tk.E+tk.W)
lbldesc.grid(row = 1, column = 0, columnspan = 2, sticky = tk.E+tk.W)
lblname.grid(row = 2, column = 0)
inptname.grid(row = 2, column = 1, sticky = tk.W)
lblstock.grid(row = 3, column = 0)
inptstock.grid(row = 3, column = 1, sticky = tk.W)
lblmanuf.grid(row = 4, column = 0)
inptmanuf.grid(row = 4, column = 1, sticky = tk.W)
lblware.grid(row = 5, column = 0)
inptware.grid(row = 5, column = 1, sticky = tk.W)
inptbtn.grid(row=6, column = 0)

menubar = tk.Menu(window)

listmenu = tk.Menu(menubar, tearoff = 0)
listmenu.add_command(label = "View List", command = viewlist)
listmenu.add_separator()
listmenu.add_command(label = "Delete List", command = clearlist)
menubar.add_cascade(label = "List Options", menu = listmenu)

menubar.add_command(label = "Credits", command = credit)
menubar.add_command(label = "Version", command = version)

window.config(menu = menubar)
window.mainloop()
