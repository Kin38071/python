# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:18:28 2022

@author: kin38071
"""
#Události
#komponenta.bind(událost,funkce)

from tkinter import *

"""
def LevyKlik(udalost):
    print("kliknuto na pozici",udalost.x,udalost.y)

def Najeti(udalost):
    print("Najel jsi na rám")
    
def Pryc(udalost):
    print("Jsi mimo")
    
def Klavesa(udalost):
    print("Stiskl jsi",udalost.char)

hlavni=Tk()

ram=Frame(hlavni,width=100,height=100,bg="black",bd=2)
ram.bind("<Button-1>",LevyKlik)
#<Button-2> = prostř. tlačítko myši, <Button-3> = pravé tlačítko
#<Double-Button-1> = dvojklik levým tlačítkem
ram.bind("<Enter>",Najeti)  #najetí myši do prostoru komponenty
ram.bind("<Leave>",Pryc)    #opuštění komponenty

vstup=Entry(hlavni)
vstup.bind("<Key>",Klavesa) #stisk klávesy s běžným znakem
vstup.pack(padx=5,pady=5)

ram.pack()

hlavni.mainloop()
"""

#Souborové dialogy a barevný dialog

from tkinter import filedialog as fld
from tkinter import colorchooser as clr


def Otevrit():
    try:
        ret=fld.askopenfilename(title="Otevřít soubor")
        #print(ret)
        soubor=open(ret,"r")
        cely=soubor.read()
        print(cely)
        soubor.close()
    except:pass

def Ulozit():
    try:
        ret=fld.asksaveasfilename(title="Uložit soubor",defaultextension="txt")
        soubor=open(ret,"w")
        soubor.write("aaaaaaaaaaaazicxzvius")
        soubor.close()
    except:pass

def Barva():
    barva=clr.askcolor(title="Výběr barvy")
    print(barva)
    hlavni["bg"]=barva[1]

hlavni=Tk()

otevrit=Button(hlavni,text="Otevřít",width=10,command=Otevrit)
otevrit.pack(padx=5,pady=5)
ulozit=Button(hlavni,text="Uložit",width=10,command=Ulozit)
ulozit.pack(padx=5,pady=5)

vyberbarvy=Button(hlavni,text="Barva",width=10,command=Barva)
vyberbarvy.pack(padx=5,pady=5)

hlavni.mainloop()