# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 08:06:31 2022

@author: kin38071
"""
from tkinter import *


#Spinbox - výběr celých čísel

"""

def Nastav():
    vypis["text"]=cislo.get()
    #vypis["text"]=c.get()


hlavni=Tk()

c=StringVar()
c.set("0")


#cislo=Spinbox(hlavni,from_=-50,to=1000,increment=5,textvariable=c,command=Nastav)
#specifikace hodnot
cislo=Spinbox(hlavni,values=(0,1,2,3,5,9,11,13,17),textvariable=c)
cislo.pack(padx=5,pady=5)

vypis=Label(hlavni,text="0",font="Arial 20",textvariable=c)
vypis.pack(padx=5,pady=5)


hlavni.mainloop()

"""

#OptionMenu - rozbalovací menu

"""

def Nastav(hodnota):
    vystup["text"]="Vybráno:"+v.get()#+hodnota

hlavni=Tk()

v=StringVar()
v.set("jedna")

vyber=OptionMenu(hlavni,v,"jedna","dva","tři",command=Nastav)
vyber.configure(width=10)
vyber.pack(padx=5,pady=5)

vystup=Label(hlavni,text="jedna")
vystup.pack(padx=5,pady=5)

hlavni.mainloop()

"""

#OptionMenu - seznam parametrů

"""

hlavni=Tk()


hodnoty=["jedna","dva","tři","čtyři"]

v=StringVar()
v.set(hodnoty[0])

vyber=OptionMenu(hlavni,v,*hodnoty)
vyber.configure(width=10)
vyber.pack(padx=5,pady=5)

hlavni.mainloop()

"""

#Standardní dialogy

from tkinter import messagebox as msb

def Zprava():
    msb.showinfo("Informace","Přečtěte si, prosím,\nnásledující informace")
    #msb.showwarning
    #msb.showerror

def Dotaz():
    x=msb.askyesno("Konec","Opravdu skončit?")  #True a False
    #msb.askokcancel
    #msb.askretrycancel
    #msb.askquestion    vrací "yes" a "no"
    if x:
        hlavni.destroy()


hlavni=Tk()

zprava=Button(hlavni,text="Zpráva",width=10,command=Zprava)
zprava.pack(padx=5,pady=5)

dotaz=Button(hlavni,text="Otázka",width=10,command=Dotaz)
dotaz.pack(padx=5,pady=5)

hlavni.mainloop()