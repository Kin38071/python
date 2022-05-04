# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:01:18 2022

@author: kin38071
"""
from tkinter import *
from tkinter import messagebox as msb

def Pocitej():
    x=cislo.get()
    y=cislo2.get()
    akce=w.get()
    if akce == hodnoty[0]:
        vypis["text"]=int(x)+int(y)
    elif akce == hodnoty[1]:
        vypis["text"]=int(x)-int(y)
    elif akce == hodnoty[2]:
        vypis["text"]=int(x)*int(y)
    elif akce == hodnoty[3]:
        if y == "0":
            msb.showerror("Upozornění","Nunou nelze dělit.")
        else:
            vypis["text"]=int(x)/int(y)


hlavni=Tk()

c=StringVar()
c.set("0")


cislo=Spinbox(hlavni,from_=-100,to=100,textvariable=c)
cislo.pack(padx=5,pady=5)

v=StringVar()
v.set("0")

cislo2=Spinbox(hlavni,from_=-100,to=100,textvariable=v)
cislo2.pack(padx=5,pady=5)

vypis=Label(hlavni,text="0",font="Arial 20")
vypis.pack(padx=5,pady=5)


hodnoty=["Součet","Rozdíl","Součin","Podíl"]

w=StringVar()
w.set(hodnoty[0])

vyber=OptionMenu(hlavni,w,*hodnoty)
vyber.configure(width=10)
vyber.pack(padx=5,pady=5)

poc=Button(hlavni,text="Počítej",width=10,command=Pocitej)
poc.pack(padx=5,pady=5)

hlavni.mainloop()