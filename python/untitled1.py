# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:45:44 2022

@author: narut
"""

from tkinter import *
from tkinter import messagebox
import random

zadano=0
priklady=0
dobre=0
x=0
y=0


def Generovat():
    global zadano
    global priklady
    global x
    global y
    if zadano==0:
        zadano=1
        priklady=priklady+1
        op=operace.get()
        if op==1:
            while True:
                x=random.randint(0,100)
                y=random.randint(0,100)
                if x+y<=100:
                    zadani["text"]=str(x)+" + "+str(y)+" ="
                    break
                else:
                    continue
        elif op==2:
            while True:
                x=random.randint(0,100)
                y=random.randint(0,100)
                if x-y>0:
                    zadani["text"]=str(x)+" - "+str(y)+" ="
                    break
                else:
                    continue
        elif op==3:
            x=random.randint(0,10)
            y=random.randint(0,10)
            zadani["text"]=str(x)+" * "+str(y)+" ="
        elif op==4:
            while True:
                x=random.randint(0,100)
                y=random.randint(1,10)
                if x/y<=10 and (x/y)%1==0:
                    zadani["text"]=str(x)+" / "+str(y)+" ="
                    break
                else:
                    continue
    elif zadano==1:
        spravne["text"]="Nelze generovat nový příklad dokud současný není vypočítaný"
        
        
def Vypocet():
    global x
    global y
    global dobre
    global zadano
    vys=vysledek.get()
    op=operace.get()
    try:
        vys=int(vys)
        if op==1:
            if x+y==vys:
                dobre=dobre+1
                spravne["text"]="Správně!"
                zadano=0
            else:
                spravne["text"]="Špatně"
                zadano=0
        elif op==2:
            if x-y==vys:
                dobre=dobre+1
                spravne["text"]="Správně!"
                zadano=0
            else:
                spravne["text"]="Špatně"
                zadano=0
        elif op==3:
            if x*y==vys:
                dobre=dobre+1
                spravne["text"]="Správně!"
                zadano=0
            else:
                spravne["text"]="Špatně"
                zadano=0
        elif op==4:
            if x/y==vys:
                dobre=dobre+1
                spravne["text"]="Správně!"
                zadano=0
            else:
                spravne["text"]="Špatně"
                zadano=0
    except ValueError:
        spravne["text"]="Prosím zadejte číslo"
        
        
        
def Vyhodnotit():
    global priklady
    global dobre
    messagebox.showinfo(title="Vyhodnocení",message=str(dobre)+"/"+str(priklady))
    hlavni.destroy()

hlavni=Tk()
hlavni.title("Počítání")

ram = LabelFrame(hlavni,relief=SUNKEN,text="Operace")
ram.grid(padx=5,pady=5)

operace=IntVar()
operace.set(1)

scitani=Radiobutton(ram,text="Sčítání",variable=operace,value=1)
scitani.pack()
odcitani=Radiobutton(ram,text="Odčítání",variable=operace,value=2)
odcitani.pack()
nasobeni=Radiobutton(ram,text="Násobení",variable=operace,value=3)
nasobeni.pack()
deleni=Radiobutton(ram,text="Dělení",variable=operace,value=4)
deleni.pack()

test=Button(hlavni,text="Generovat Příklad",command=Generovat)
test.grid(row=0,column=1,padx=5,pady=5)

zadani=Label(hlavni,text="Příklad")
zadani.grid(row=1,column=0,padx=5,pady=5)

vysledek=Entry(hlavni)
vysledek.grid(row=1,column=1,padx=5,pady=5)

spravne=Label(hlavni,text="")
spravne.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

potvrdit=Button(hlavni,text="Potvrdit výsledek",command=Vypocet)
potvrdit.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

konec=Button(hlavni,text="Vyhodnotit a ukončit",command=Vyhodnotit)
konec.grid(row=4,column=0,columnspan=2,padx=5,pady=5)

zadano=0

hlavni.mainloop()