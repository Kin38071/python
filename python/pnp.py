# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 08:11:49 2022

@author: kin38071
"""
#Graf ze souboru

from tkinter import *
from tkinter import filedialog as fld
from tkinter import messagebox as msb
import pylab as py

#Funkce pro výběr souboru
def VyberSoubor():
    global cesta
    cesta=fld.askopenfilename(title="Vyberte soubor")
    if cesta!="":
        souborCesta.set(cesta)

#Funkce pro čtení ze souboru a vykreslení grafu
def FceSoubor():
    try:
        soubor=open(cesta,"r")
        nazev=soubor.readline()
        osaX=soubor.readline()
        osaY=soubor.readline()
        cislaX=[]
        cislaY=[]
        while True:
            radek=soubor.readline()
            if radek=="":
                break
            cisla=radek.split()
            cislaX.append(float(cisla[0]))
            cislaY.append(float(cisla[1]))
        soubor.close()
        x=py.array(cislaX)
        y=py.array(cislaY)
        py.plot(x,y)
        py.title(nazev)
        py.xlabel(osaX)
        py.ylabel(osaY)
        py.grid(True)
        py.show()
    except:
        msb.showerror("Chybný formát souboru","Graf se nepodařilo vytvořit \nzkontrolujte formát souboru")


hlavni=Tk()
hlavni.title("Graf ze souboru")

#Vzhled aplikace
souborRam=LabelFrame(hlavni,text="Graf ze souboru",bd=2,relief="ridge")
souborRam.grid(padx=5,pady=5)

souborCesta=StringVar()
souborCesta.set("\cesta\k\souboru")

vstupgraf=Entry(souborRam,textvariable=souborCesta)
vstupgraf.pack(padx=5,pady=5)

otevrit=Button(souborRam,text="Vyber soubor pro graf",width=20,command=VyberSoubor)
otevrit.pack(padx=10,pady=10)

vytvorgraf=Button(hlavni,text="Vytvoř graf",width=15,height=5,command=FceSoubor)
vytvorgraf.grid(row=0,column=1,padx=10)




















hlavni.mainloop()