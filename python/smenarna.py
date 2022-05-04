# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:11:41 2022

@author: Jan Kindl
"""

from tkinter import *
from tkinter import messagebox as msb

def Vypocti():
    try:
        operace=transakce.get()
        mena=meny.get()
        hodnota=float(castka.get())
        if operace==0:      #při nákupu
            #vypocet zakladnich hodnota
            if mena=="USD":
                zaklad=22.46*hodnota
            if mena=="AUD":
                zaklad=16.86*hodnota
            if mena=="EUR":
                zaklad=24.68*hodnota
            if mena=="GBP":
                zaklad=29.61*hodnota
            if mena=="JPY":
                zaklad=0.18*hodnota
            #pridani poplatku 0.5%
            poplatek=0.005*zaklad
            celkem=zaklad-poplatek
            #zaokrouhleni
            zaklad=round(zaklad,1)
            poplatek=round(poplatek,1)
            celkem=round(celkem,1)
            #pridani jednoho desetineho mista
            zaklad=format(zaklad,'.2f')
            poplatek=format(poplatek,'.2f')
            celkem=format(celkem,'.2f')
            #vypsani info
            vysledek["text"]="Základní cena: "+zaklad+"\nPoplatek: "+poplatek+"\nCelková částka vyplacena: "+celkem
        elif operace==1:    #při prodeji
            #vypocet zakladnich hodnota
            if mena=="USD":
                zaklad=22.46*hodnota
            if mena=="AUD":
                zaklad=16.86*hodnota
            if mena=="EUR":
                zaklad=24.68*hodnota
            if mena=="GBP":
                zaklad=29.61*hodnota
            if mena=="JPY":
                zaklad=0.18*hodnota
            #pridani poplatku 0.5%
            poplatek=0.005*zaklad
            celkem=zaklad+poplatek
            #zaokrouhleni
            zaklad=round(zaklad,1)
            poplatek=round(poplatek,1)
            celkem=round(celkem,1)
            #pridani jednoho desetineho mista
            zaklad=format(zaklad,'.2f')
            poplatek=format(poplatek,'.2f')
            celkem=format(celkem,'.2f')
            #vypsani info
            vysledek["text"]="Základní cena: "+zaklad+"\nPoplatek: "+poplatek+"\nCelková částka k zaplacení: "+celkem
    except ValueError:
        msb.showerror(title="Chyba",message="Nastala chyba!\nProsím zadávejte pouze čísla.\nPokud zadáváte desetinná čísla, použijte desetinnou tečku místo čárky.")

hlavni=Tk()

Label(hlavni,text="Směnárna").grid(padx=5,pady=5,columnspan=10)

kp=LabelFrame(hlavni,text="Transakce")
kp.grid(row=1,padx=5,pady=5)

transakce=IntVar()
transakce.set(0)
kup=Radiobutton(kp,text="Nákup",variable=transakce,value=0)
kup.pack(padx=3,pady=3)
prodej=Radiobutton(kp,text="Prodej",variable=transakce,value=1)
prodej.pack(padx=3,pady=3)

mena=LabelFrame(hlavni,text="Měna")
mena.grid(row=1,column=1,padx=5,pady=5,columnspan=10)
meny=StringVar()
meny.set("USD")
menymenu=OptionMenu(mena,meny,"USD","AUD","EUR","GBP","JPY")
menymenu.pack(padx=5,pady=5)

Label(hlavni,text="Zadejte částku, kterou chcete nakoupit/prodat").grid(padx=5,pady=5,row=2,column=0,columnspan=10)


castka=Entry(hlavni)
castka.grid(row=3,column=0,padx=5,pady=5,columnspan=10)
castka.insert(END, 0)

vypocet=Button(hlavni,text="Výpočet",command=Vypocti)
vypocet.grid(row=4,column=0,padx=5,pady=5,columnspan=10)

vysledek=Label(hlavni,text="")
vysledek.grid(row=5,column=0,padx=5,pady=5,columnspan=10)


kurzlistekram=LabelFrame(hlavni,text="Kurzovní lístek",labelanchor="n")
kurzlistekram.grid(row=6,column=0,padx=5,pady=5,columnspan=10)

kurzlistek=Text(kurzlistekram,width=30,height=5)
kurzlistek.pack(padx=5,pady=5)
kurzlistek.insert(END,"USD - 22,46")
kurzlistek.insert(END,"\n")
kurzlistek.insert(END,"AUD - 16,86")
kurzlistek.insert(END,"\n")
kurzlistek.insert(END,"EUR - 24,68")
kurzlistek.insert(END,"\n")
kurzlistek.insert(END,"GBP - 29,61")
kurzlistek.insert(END,"\n")
kurzlistek.insert(END,"JPY - 0,18")
kurzlistek.config(state=DISABLED)

hlavni.mainloop()