from tkinter import *
from mail import *
from tkinter import ttk
root=Tk()
me=Menu(root)
root.geometry('600x600')

rows = 0
while rows < 50:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1

root.config(menu=me)
file=Menu(me)
me.add_cascade(label="File",menu=file)
file.add_command(label="Setup",command = set)
file.add_command(label="Start",command = start)

def go():
    us=userw.get()
    ps=passw.get()
    setdt(us,ps,"Whatever")

nb=ttk.Notebook(root)
nb.grid(row=1,column=0,columnspan=50,rowspan=49,sticky='NESW')

tab1=ttk.Frame(nb)
nb.add(tab1, text="Setup")
tab2=ttk.Frame(nb)
nb.add(tab2,text="Configure")
    
label1=Label(tab1,text="Username")
userw=Entry(tab1, bd=5,width=40)
label2=Label(tab1,text="Password")
passw=Entry(tab1, bd=5,width=40,show="*")
submit= Button(tab1,text="Submit",command=go)
stop=Button(tab1,text="Stop")

label1.grid(row=0,column=0)
userw.grid(row=0,column=1)
label2.grid(row=1,column=0)
passw.grid(row=1,column=1)
submit.grid(row=2,column=0)
stop.grid(row=2,column=1)

root.mainloop()

