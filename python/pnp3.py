# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 08:14:09 2022

@author: kin38071
"""
#Práce se souubory

from tkinter import *
from tkinter import messagebox as msb
from tkinter import filedialog as fld

def Otevrit():
    cesta=fld.askopenfilename(title="Vyberte soubor")
    if cesta!="":
        souborO=open(cesta,"r")
        obsah=souborO.read()
        text.delete(1.0,END)
        text.insert(1.0,obsah)
        souborO.close()

def Ulozit():
    f = fld.asksaveasfile(mode='w', defaultextension=".txt")
    if f!="":
        tts = str(text.get(1.0, END))
        f.write(tts)
        f.close()

#Funkce pro ukončení apliacec s dotazem
def Konec():
    x=msb.askyesno("Konec aplikace","Operavdu chcete skončit?")
    if x:
        hlavni.destroy()

#Funkce pro převod písmen na velká
def Velka():
    a=text.get(1.0,END)
    a=a.upper()
    text.delete(1.0,END)
    text.insert(1.0,a)

#Funkce pro okno nahrazení
def OknoNahrad():
    global vstup1
    global vstup2
    global oknoN
    oknoN=Toplevel()    #vytvoření vnořeného okna
    t1=Label(oknoN,text="Nahradit znak")
    t1.pack(padx=3,pady=3)
    vstup1=Entry(oknoN)
    vstup1.pack(padx=3,pady=3)
    t2=Label(oknoN,text="Tímto znakem")
    t2.pack(padx=3,pady=3)
    vstup2=Entry(oknoN)
    vstup2.pack(padx=3,pady=3)
    akce=Button(oknoN,text="Proveď",width=10,command=Nahradit)
    akce.pack(padx=3,pady=3)
    
    
#Funkce pro nahrazení znaku
def Nahradit():
    ret=text.get(1.0,END)
    ret1=ret.replace(vstup1.get(),vstup2.get())
    text.delete(1.0,END)
    text.insert(1.0,ret1)
    oknoN.destroy()    

#Funkce pro statistiku znaků
def OknoStatistika():
    seznam=[]
    oknoS=Toplevel()
    texts=Text(oknoS,font="Arial 10",width=20,height=30)
    texts.pack(padx=3,pady=3)
    radky=text.get(1.0,END)
    radky=radky.lower()
    for i in radky:
        seznam.append(i)
    for i in abeceda:
        texts.insert(END,i+": ")
        texts.insert(END,str(seznam.count(i)))
        texts.insert(END,"\n")


hlavni=Tk()

abeceda="abcdefghijklmnopqrstuvwxyz"

text=Text(hlavni,font="Arial 10")
text.pack()

hornimenu=Menu(hlavni)
menusoubor=Menu(hornimenu,tearoff=0)
menusoubor.add_command(label="Otevřít",command=Otevrit)
menusoubor.add_command(label="Uložit",command=Ulozit)
menusoubor.add_separator()
menusoubor.add_command(label="Konec",command=Konec)
hornimenu.add_cascade(label="Soubor",menu=menusoubor)

menuoperace=Menu(hornimenu,tearoff=0)
menuoperace.add_command(label="Velká písmena",command=Velka)
menuoperace.add_command(label="Nahradit znak",command=OknoNahrad)
menuoperace.add_command(label="Statistika znaků",command=OknoStatistika)
hornimenu.add_cascade(label="Operace",menu=menuoperace)

hlavni.config(menu=hornimenu)

hlavni.mainloop()