# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:59:41 2022

@author: kin38071
"""
from tkinter import *
import random

def Levy(udalost):
    ram["bg"]="white"

def Pravy(udalost):
    barva ="#"+"%06x" % random.randint(0, 0xFFFFFF)
    ram["bg"]=barva

#1
hlavni=Tk()

ram=Frame(hlavni,width=100,height=100,bg="white",bd=2)
ram.bind("<Button-1>",Levy)
ram.bind("<Button-3>",Pravy)

ram.pack()

hlavni.mainloop()


#2
from tkinter import filedialog as fld

def Ulozit():
    try:
        ret=fld.asksaveasfilename(title="Uložit soubor",defaultextension="txt")
        soubor=open(ret,"w")
        for i in range(100):
            barva ="#"+"%06x" % random.randint(0, 0xFFFFFF)
            soubor.write(barva)
            soubor.write("\n")
        soubor.close()
    except:pass







hlavni=Tk()

ulozit=Button(hlavni,text="Uložit",width=10,command=Ulozit)
ulozit.pack(padx=5,pady=5)

hlavni.mainloop()