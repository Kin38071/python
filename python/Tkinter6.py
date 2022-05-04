# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 08:07:00 2022

@author: kin38071
"""
#Menu

from tkinter import *
from tkinter import messagebox as msb

def Hlaska(a):
    msb.showinfo(a,"Není naprogramováno")

def Pokus():
    if v1.get()==1:
        vystup1["text"]="Zapnuto"
    else:
        vystup1["text"]="Vypnuto"

def Prep():
    vystup2["text"]=vyber[v2.get()]



hlavni=Tk()
hlavni.minsize(300,80)


hornimenu=Menu(hlavni)

#hornimenu.add_command(label="Soubor",command=lambda:Hlaska("Soubor"))

#vytvoření rozbalovací nabídky a připojení ho do hlavního menu
menuSoubor=Menu(hornimenu,tearoff=0)
menuSoubor.add_command(label="Otevřít")
menuSoubor.add_command(label="Uložit")
menuSoubor.add_separator()      #oddělovač
menuSoubor.add_command(label="Konec",command=hlavni.destroy)

hornimenu.add_cascade(label="Soubor",menu=menuSoubor)

#další rozbalovací menu 
menuUpravy=Menu(hornimenu,tearoff=0)
menuUpravy.add_command(label="Vyjmout")
menuUpravy.add_command(label="Kopírovat")
menuUpravy.add_command(label="Vložit")
menuUpravy.add_separator()


v1=IntVar()
menuUpravy.add_checkbutton(label="Pokus",variable=v1, command=Pokus)


menuUpravy.add_separator()



v2=IntVar()
vyber=["první","druhý","třetí"]

menuUpravy.add_radiobutton(label="1",variable=v2,value=0,command=Prep)
menuUpravy.add_radiobutton(label="2",variable=v2,value=1,command=Prep)
menuUpravy.add_radiobutton(label="3",variable=v2,value=2,command=Prep)


hornimenu.add_cascade(label="Úpravy",menu=menuUpravy)


hornimenu.add_command(label="Nastavení",command=lambda:Hlaska("Nastavení"))
hornimenu.add_command(label="Nápověda",command=lambda:Hlaska("Nápověda"))
hornimenu.add_command(label="Konec", command=hlavni.destroy)

hlavni.config(menu=hornimenu)   #bude zobrazeno právě hornimenu


vystup1=Label(hlavni,text="Vypnuto",font="Arial 12 bold")
vystup1.pack(padx=10,pady=10)

vystup2=Label(hlavni,text=vyber[0],font="Arial 12 bold")
vystup2.pack(padx=10,pady=10)


hlavni.mainloop()