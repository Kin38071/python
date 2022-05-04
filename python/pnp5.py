# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 08:06:24 2022

@author: kin38071
"""
#Výpočet funkční hodnoty podle vzorce se zadanými parametry

from tkinter import *
import math as mt

def Vyp_fce():
    m=int(vstupM.get())
    n=int(vstupN.get())
    x=float(vstupX.get())
    g=n-m+1
    y=0
    for i in range(g):
        y=y+5*(mt.cos(3*x))
    vysledek["text"]=str(y)


hlavni=Tk()

#Vzhled aplikace
ram=LabelFrame(hlavni,text="Výpočet funkční hodnoty",bd=2,relief="ridge",padx=10,pady=10)
ram.pack(padx=5,pady=5)

popisM=Label(ram,text="Zadej hodnotu m (celé číslo)",font="Calibri 10")
popisM.grid(padx=5)
vstupM=Entry(ram,font="Calibri 10")
vstupM.grid(row=1,pady=5)

popisN=Label(ram,text="Zadej hodnotu n (celé číslo)",font="Calibri 10")
popisN.grid(row=2,padx=5)
vstupN=Entry(ram,font="Calibri 10")
vstupN.grid(row=3,pady=5)

popisX=Label(ram,text="Zadej hodnotu x (reálné číslo)",font="Calibri 10")
popisX.grid(row=4,padx=5)
vstupX=Entry(ram,font="Calibri 10")
vstupX.grid(row=5,pady=5)

vypocet_fce=Button(ram,text="Proveď \nvýpočet",font="Calibri 10 bold",command=Vyp_fce)
vypocet_fce.grid(row=1,column=1,rowspan=5,sticky=N+S,padx=5,pady=5)

vysledek=Label(ram,text="Výsledek",font="Calibri 12 bold",bg="lightblue")
vysledek.grid(row=6,columnspan=2,sticky=E+W,pady=5)

hlavni.mainloop()