from tkinter import *
def add1():
    a=float(e1.get())
    b=float(e2.get())
    c=a+b
    t1.delete("1.0",END)
    t1.insert(END,c)
abc=Tk()
a_e=StringVar()
b_e=StringVar()
l1=Label(abc,text="a")
l1.grid(row=0,column=0)
l2=Label(abc,text="b")
l2.grid(row=1,column=0)
l3=Label(abc,text="c")
l3.grid(row=2,column=0)
e1=Entry(abc,textvariable=a_e)
e1.grid(row=0,column=1)
e2=Entry(abc,textvariable=b_e)
e2.grid(row=1,column=1)
b1=Button(abc,text="add",command=add1,justify='center')
b1.grid(row=3,column=0,columnspan=1,padx=15)
t1=Text(abc,height=3,width=5)
t1.grid(row=2,column=1)
abc.mainloop()
