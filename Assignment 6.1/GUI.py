from tkinter import *
win = Tk()
 
valt1 = StringVar()
valt2 = StringVar()
val1 = StringVar()
val2 = StringVar()

lab1 = Label(win,textvariable = valt1).grid(row = 1, column = 0)
lab2 = Label(win,textvariable = valt2).grid(row = 2, column = 0)

txt1 = Entry(win,textvariable = val1, width=35).grid(row = 1, column = 1,columnspan = 3)
txt2 = Entry(win,textvariable = val2, width=35).grid(row = 2, column = 1,columnspan = 3)

def kgconvert():
    valt1.set("Kilogram")
    valt2.set("Gram")
    
    if val1.get()!= "":
        v1 = int(val1.get())
        v2 = v1*1000
        val2.set(v2)
    else:
        if val2.get()!="":
            v2 = int(val2.get())
            v1 = v2/1000
            val1.set(v1)
   
def pgconvert():
    valt1.set("Pound")
    valt2.set("miligrams")
    
    if val1.get()!= "":
        v1 = int(val1.get())
        v2 = float(v1/(0.0000022))
        val2.set(v2)
    else:
        if val2.get()!="":
            v2 = int(val2.get())
            v1 = v2*(0.0000022)
            val1.set(v1)
win.geometry("400x200")
win.title('calculator')
kg = Button(win, text="Kilograms",command = kgconvert,bg='light slate blue',height=1,width=10).grid(row = 3,column = 0,padx=10,pady=10)
pound = Button(win, text="Pound",command = pgconvert,bg='light slate blue',height=1,width=10).grid(row = 3,column = 1,padx=10,pady=10)
win.mainloop()