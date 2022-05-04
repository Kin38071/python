# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 08:08:05 2022

@author: kin38071
"""
from tkinter import *
import pylab as pl

#Grafy matematických funkcí

def Graf_fce():
    x_min=float(vstup_xmin.get())
    x_max=float(vstup_xmax.get())
    x_min=pl.radians(x_min)
    x_max=pl.radians(x_max)
    x=pl.arange(x_min,x_max,0.1)
    if vyberF.get()==vyber_fce[0]:
        y=pl.sin(x)
    elif vyberF.get()==vyber_fce[1]:
        y=pl.sin(x/2)
    else:
        y=pl.sin(2*x)
    pl.plot(x,y)
    pl.show()
        
        
        


hlavni=Tk()

#Seznam pro výběr funkcí
vyber_fce=["f(x)=sin(x)","f(x)=sin(x/2)","f(x)=sin(2x)"]

#Vzhled aplikace
vyberF=StringVar()
vyberF.set(vyber_fce[0])

ram=LabelFrame(hlavni,text="Průběh matematické funkce",font="Calibri 10",bd=2,relief="ridge",padx=10,pady=10)
ram.pack(padx=5,pady=5)

popis_vyber=Label(ram,text="Výběr funkce:",font="Calibri 10")
popis_vyber.grid(columnspan=2,sticky=W+E)
vyber=OptionMenu(ram, vyberF, *vyber_fce)
vyber.config(font="Calibri 12")
vyber.grid(row=1,columnspan=2,sticky=W+E,pady=5)

popis_xmin=Label(ram,text="Min. hodnota x [stupně]",font="Calibri 10")
popis_xmin.grid(row=2)
vstup_xmin=Entry(ram,font="Calibri 10")
vstup_xmin.grid(row=3,pady=5)

popis_xmax=Label(ram,text="Max. hodnota x [stupně]",font="Calibri 10")
popis_xmax.grid(row=4)
vstup_xmax=Entry(ram,font="Calibri 10")
vstup_xmax.grid(row=5,pady=5)

graf=Button(ram,text="Vykresli \ngraf",font="Calibri 10 bold",command=Graf_fce)
graf.grid(row=2,column=1,rowspan=4,sticky=N+S,padx=5)

hlavni.mainloop()