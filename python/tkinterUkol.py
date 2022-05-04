# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 08:39:23 2021

@author: kin38071
"""
from tkinter import *
import random

def Soucet():
    x=random.randint(1,10)
    y=random.randint(1,10)
    napis["text"]="{}+{}={}".format(x,y,x+y)
    napis["fg"]="green"

def Rozdil():
    x=random.randint(1,10)
    y=random.randint(1,10)
    napis["text"]="{}-{}={}".format(x,y,x-y)
    napis["fg"]="blue"

def Soucin():
    x=random.randint(1,10)
    y=random.randint(1,10)
    napis["text"]="{}*{}={}".format(x,y,x*y)
    napis["fg"]="grey"

def Podil():
    x=random.randint(1,10)
    y=random.randint(1,10)
    napis["text"]="{}/{}={}".format(x,y,x/y)
    napis["fg"]="red"

hlavni=Tk()

napis=Label(hlavni,text="",fg="green",bg="black",width=20,height=5,font="Arial 12 bold")
napis.pack(padx=10,pady=10)

soucet=Button(hlavni,text="Součet",width=15,command=Soucet)
soucet.pack(padx=5,pady=5)

rozdil=Button(hlavni,text="Rozdíl",width=15,command=Rozdil)
rozdil.pack(padx=5,pady=5)

soucin=Button(hlavni,text="Součin",width=15,command=Soucin)
soucin.pack(padx=5,pady=5)

podil=Button(hlavni,text="Podíl",width=15,command=Podil)
podil.pack(padx=5,pady=5)

konec=Button(hlavni,text="Konec",width=15,command=hlavni.destroy)
konec.pack(padx=10,pady=10)

hlavni.mainloop()