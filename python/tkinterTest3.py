# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 08:09:04 2022

@author: kin38071
"""
from tkinter import *
from tkinter import messagebox

#1

def Prevod():
    try:
        jedn=str(hodnota.get())
        cislo=float(vstup.get())
        if cislo<0:
            messagebox.showerror("Chyba", "Nepřevádějte záporná čísla")
        else:
            if jedn=="l":
                vysledek=cislo*0.1
            elif jedn=="cl":
                vysledek=cislo*10
            elif jedn=="ml":
                vysledek=cislo*100
            vypis["text"]=vysledek,jedn
    except ValueError:
        messagebox.showerror("Chyba", "Zadávejte pouze čísla.")





hlavni=Tk()

Label(hlavni,text="dl: ").grid(row=0,column=0)

vstup=Entry()
vstup.grid(row=0,column=1,padx=5,pady=5)

hodnota=StringVar()
hodnota.set("l")

Label(hlavni,text="na").grid(row=0,column=2)

menu=OptionMenu(hlavni,hodnota,"l","cl","ml")
menu.grid(row=0,column=3,padx=5,pady=5)

tlc=Button(hlavni,text="Převod",width=10,command=Prevod)
tlc.grid(row=1,column=0,padx=5,pady=5,columnspan=4)

vypis=Label(hlavni,text="",font="Arial 20")
vypis.grid(row=2,column=0,padx=5,pady=5,columnspan=4)

hlavni.mainloop()

#2

def Mena():
    try:
        hodnota=float(vstup.get())
        prevod=int(meny.get())
        if hodnota<0:
            messagebox.showerror("Chyba", "Nepřevádějte záporná čísla")
        else:
            if prevod==1:
                vysledek=hodnota*0.293083
                zkr="CNY"
            elif prevod==2:
                vysledek=hodnota*10000
                zkr="VEF"
            elif prevod==3:
                vysledek=hodnota*0.640615
                zkr="ZAR"
            vypis["text"]=vysledek,zkr
    except ValueError:
        messagebox.showerror("Chyba", "Zadávejte pouze čísla.")

hlavni=Tk()

Label(hlavni,text="CZK: ").grid(row=1,column=0,sticky=E)

vstup=Entry()
vstup.grid(row=1,column=1,padx=5,pady=5)

Label(hlavni,text="na").grid(row=1,column=2)

meny=IntVar()
meny.set(1)

prvni=Radiobutton(hlavni,text="Čínský jüan", variable=meny,value=1)
prvni.grid(row=0,column=3,padx=5,pady=5,sticky=W)

druhy=Radiobutton(hlavni,text="Venezuelský bolívar", variable=meny,value=2)
druhy.grid(row=1,column=3,padx=5,pady=5,sticky=W)

treti=Radiobutton(hlavni,text="Jihoafrický rand", variable=meny,value=3)
treti.grid(row=2,column=3,padx=5,pady=5,sticky=W)

tlc=Button(hlavni,text="Převod",width=10,command=Mena)
tlc.grid(row=3,column=0,padx=5,pady=5,columnspan=4)

vypis=Label(hlavni,text="",font="Arial 20")
vypis.grid(row=4,column=0,padx=5,pady=5,columnspan=4)

hlavni.mainloop()