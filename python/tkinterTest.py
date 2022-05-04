# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:08:02 2021

@author: kin38071
"""
from tkinter import *
import random

def Vypocitat():
    a=float(vstup1.get())
    b=float(vstup2.get())
    if a==0:
        vysledek["text"]="Rovnice nemá řešení"
    else:
        vysledek["text"]="x= "+str(round(-b/a,2))
    vstup1.select_range(0,END)

def Generovat():
    while True:
        x=random.randint(1,100)
        y=random.randint(1,100)
        if x+y<100:
            break
        else:
            continue
    zadani["text"]=str(x)+" + "+str(y)+" = "
    global zkontrolovat
    zkontrolovat=x+y
    
def Kontrola():
    vypocet=int(vysledek.get())
    global zkontrolovat
    if zkontrolovat==vypocet:
        vypis["text"]="SPRÁVNĚ!"
    else:
        vypis["text"]="ŠPATNĚ!"
    
    
#1
hlavni=Tk()

titul=Label(hlavni,text="ax+b=0")
titul.grid(row=0,column=0,columnspan=2,sticky=W+E,padx=5,pady=5) 

cislo1=Label(hlavni,text="hodnota a:")
cislo1.grid(row=1,column=0)        
                                     
cislo2=Label(hlavni,text="hodnota b:")
cislo2.grid(row=2,column=0)

vstup1=Entry(hlavni)
vstup1.grid(row=1,column=1,padx=5,pady=5)

vstup2=Entry(hlavni)
vstup2.grid(row=2,column=1,padx=5,pady=5)


vypocet=Button(hlavni,text="Výpočet",width=10,command=Vypocitat)
vypocet.grid(row=3,column=0,columnspan=2,sticky=W+E,padx=5,pady=5)

vysledek=Label(hlavni,text="x= ")
vysledek.grid(row=4,column=0,columnspan=2,sticky=W+E,padx=5,pady=5)  

konec=Button(hlavni,text="Konec",width=15,command=hlavni.destroy)
konec.grid(row=5,column=0,columnspan=2,sticky=W+E,padx=5,pady=5)

hlavni.mainloop()
#2

hlavni=Tk()

hlavni.title("Sčítání")

tlacitko=Button(hlavni,text="Generovat",width=10,command=Generovat)
tlacitko.grid(row=0,column=0,columnspan=2,sticky=W+E,padx=5,pady=5)


zadani=Label(hlavni,text="x + y = ")
zadani.grid(row=1,column=0) 

vysledek=Entry(hlavni)
vysledek.grid(row=1,column=1,padx=5,pady=5) 

vypis=Label(hlavni,text="")
vypis.grid(row=2,column=0,columnspan=2,sticky=W+E,padx=5,pady=5)

kontrola=Button(hlavni,text="Kontrola",width=10,command=Kontrola)
kontrola.grid(row=3,column=0,columnspan=2,sticky=W+E,padx=5,pady=5)

konec=Button(hlavni,text="Konec",width=15,command=hlavni.destroy)
konec.grid(row=4,column=0,columnspan=2,sticky=W+E,padx=5,pady=5)

hlavni.mainloop()