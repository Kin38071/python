# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:07:17 2022

@author: kin38071
"""
from tkinter import *
import random
#1

hlavni = Tk()
hlavni.configure(width=400,height=300,bg="#000000")
hlavni.resizable(FALSE,FALSE)

prvni=Label(hlavni,text="o", bg="#000000",font="Arial 20 bold",fg="blue")
prvni.place(x=random.randint(10,380),y=random.randint(10,270))

druhy=Label(hlavni,text="o", bg="#000000",font="Arial 20 bold",fg="red")
druhy.place(x=random.randint(10,380),y=random.randint(10,270))

treti=Label(hlavni,text="o", bg="#000000",font="Arial 20 bold",fg="green")
treti.place(x=random.randint(10,380),y=random.randint(10,270))

ctvrty=Label(hlavni,text="o", bg="#000000",font="Arial 20 bold",fg="yellow")
ctvrty.place(x=random.randint(10,380),y=random.randint(10,270))

paty=Label(hlavni,text="o", bg="#000000",font="Arial 20 bold",fg="white")
paty.place(x=random.randint(10,380),y=random.randint(10,270))

sesty=Label(hlavni,text="o", bg="#000000",font="Arial 20 bold",fg="pink")
sesty.place(x=random.randint(10,380),y=random.randint(10,270))

sedmy=Label(hlavni,text="o", bg="#000000",font="Arial 20 bold",fg="brown")
sedmy.place(x=random.randint(10,380),y=random.randint(10,270))

osmy=Label(hlavni,text="o", bg="#000000",font="Arial 20 bold",fg="purple")
osmy.place(x=random.randint(10,380),y=random.randint(10,270))

hlavni.mainloop()

#2

hlavni = Tk()
hlavni.resizable(FALSE,FALSE)

vstup=Entry(hlavni,width=20)
vstup.focus_set()
vstup.grid(row=0,column=0,columnspan=3,sticky=W+E)

b1=Button(hlavni,text="1", width=5, command=lambda: vstup.insert("end","1"))
b1.grid(row=1,column=0,sticky=W+E)

b2=Button(hlavni,text="2", width=5, command=lambda: vstup.insert("end","2"))
b2.grid(row=1,column=1,sticky=W+E)

b3=Button(hlavni,text="3", width=5, command=lambda: vstup.insert("end","3"))
b3.grid(row=1,column=2,sticky=W+E)

b4=Button(hlavni,text="4", width=5, command=lambda: vstup.insert("end","4"))
b4.grid(row=2,column=0,sticky=W+E)

b5=Button(hlavni,text="5", width=5, command=lambda: vstup.insert("end","5"))
b5.grid(row=2,column=1,sticky=W+E)

b6=Button(hlavni,text="6", width=5, command=lambda: vstup.insert("end","6"))
b6.grid(row=2,column=2,sticky=W+E)

b7=Button(hlavni,text="7", width=5, command=lambda: vstup.insert("end","7"))
b7.grid(row=3,column=0,sticky=W+E)

b8=Button(hlavni,text="8", width=5, command=lambda: vstup.insert("end","8"))
b8.grid(row=3,column=1,sticky=W+E)

b9=Button(hlavni,text="9", width=5, command=lambda: vstup.insert("end","9"))
b9.grid(row=3,column=2,sticky=W+E)

b10=Button(hlavni,text="*", width=5, command=lambda: vstup.insert("end","*"))
b10.grid(row=4,column=0,sticky=W+E)

b11=Button(hlavni,text="0", width=5, command=lambda: vstup.insert("end","0"))
b11.grid(row=4,column=1,sticky=W+E)

b12=Button(hlavni,text="#", width=5, command=lambda: vstup.insert("end","#"))
b12.grid(row=4,column=2,sticky=W+E)

smaz=Button(hlavni,text="Smaž", width=5,command=lambda: vstup.delete(0, 'end'))
smaz.grid(row=5,column=0,columnspan=3,sticky=W+E)

konec=Button(hlavni,text="Konec", width=5,command=hlavni.destroy)
konec.grid(row=0,column=3,rowspan=6,sticky=N+S+E+W)

hlavni.mainloop()