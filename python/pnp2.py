# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 08:04:14 2022

@author: kin38071
"""
#Graf podle zadání uživatele

from tkinter import *
import pylab as py

#Ukládání souřadnic do seznamů
def Uloz():
    global x_ove
    global y_ove
    x_ove.append(float(bodx.get()))
    y_ove.append(float(body.get()))
    vstupx.delete(0,END)
    vstupx.focus_set()
    vstupy.delete(0,END)
    vypis.delete(1.0,END)
    vypis.insert(1.0,x_ove)
    vypis.insert(END,"\n")
    vypis.insert(END,y_ove)

def Graf():
    x=py.array(x_ove)
    y=py.array(y_ove)
    py.plot(x,y)
    py.show()

hlavni=Tk()
hlavni.title("Grafy II")

#proměnné pro souřadnice
bodx=StringVar()
body=StringVar()
x_ove=[]
y_ove=[]

#Vzhled aplikace - zadávání souřadnic
ram=LabelFrame(hlavni,text="Zadání souřadnic",bd=2,relief="ridge",padx=5,pady=5)
ram.pack(padx=10,pady=10)

popis1=Label(ram,text="Souřadnice x",font="Calibri 10")
popis1.grid(pady=3)
vstupx=Entry(ram,font="Calibri 10", textvariable=bodx)
vstupx.grid(row=0,column=1,pady=3)

popis2=Label(ram,text="Souřadnice y",font="Calibri 10")
popis2.grid(row=1,pady=3)
vstupy=Entry(ram,font="Calibri 10", textvariable=body)
vstupy.grid(row=1,column=1,pady=3)


uloz=Button(ram,text="Ulož a další",width=15,font="Calibri 12",command=Uloz)
uloz.grid(row=2,columnspan=2,pady=2)

kresligraf=Button(hlavni,text="Vykresli graf",width=15,font="Calibri 12 bold",command=Graf)
kresligraf.pack(pady=10)

#Pro zobrazení zadávaných souřadnic
vypis=Text(hlavni,height=4,width=50)
vypis.pack()



hlavni.mainloop()