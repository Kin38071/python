"""
#tkProměnné - IntVar (celá čísla), StringVar (texty), BooleanVar (logická hodnota),
#DoubleVar (reálná čísla)

from tkinter import *

def Vypis():
    print(vstup.get())     #získání hodnoty z Entry pomocí identifikátoru komponenty
    print(t.get())         #pomocí připojené proměnné
    t.set("Něco jiného")   #nastavení textu v Entry

hlavni=Tk()

t=StringVar()              #vytvoření tkProměnné
t.set("Nějaký text")       #nastavení výchozí hodnoty (co bude v Entry po spuštění)

vstup=Entry(hlavni,textvariable=t)    #připojení proměnné
vstup.pack(padx=10,pady=10)

akce=Button(hlavni,text="Výpis",width=10,command=Vypis)
akce.pack(padx=10,pady=10)


hlavni.mainloop()

#Checkbutton - zatržítko

from tkinter import *

def Kontrola():
    if v.get()==1:                #if v.get():    (pokud by v bylo BooleanVar)
        vystup["text"]="Zapnuto"
    else:
        vystup["text"]="Vypnuto"

hlavni=Tk()

v=IntVar()    #BooleanVar()
v.set(1)      #po spuštění Checkbutton zatržen

volba=Checkbutton(hlavni,text="Zatržítko",variable=v)
volba.grid(row=0,column=1)

akce=Button(hlavni,text="Kontrola",width=10,command=Kontrola)
akce.grid(row=0,column=0,padx=5,pady=5)

vystup=Label(hlavni,text="Kontrola")
vystup.grid(row=1,columnspan=2)

hlavni.mainloop()


#Radiobutton - přepínač

from tkinter import *

def Nastav():
    v.set(2)

def Kontrola():
    if v.get()==1:
        vystup["text"]="První"
    elif v.get()==2:
        vystup["text"]="Druhá"
    else:
        vystup["text"]="Třetí"

hlavni=Tk()

v=IntVar()
v.set(1)

vyber=Frame(hlavni,bd=2,relief="ridge")
vyber.grid(row=0,rowspan=2)

Radiobutton(vyber,text="Jedna",variable=v,value=1).pack(anchor=W)
Radiobutton(vyber,text="Dva",variable=v,value=2).pack(anchor=W)
Radiobutton(vyber,text="Tři",variable=v,value=3).pack(anchor=W)

akce1=Button(hlavni,text="Kontrola",width=10,command=Kontrola)
akce1.grid(row=0,column=1,sticky=N)

akce2=Button(hlavni,text="Nastavení",width=10,command=Nastav)
akce2.grid(row=1,column=1,sticky=S)

vystup=Label(hlavni,text="Kontrola")
vystup.grid(row=2,columnspan=2,pady=10)

hlavni.mainloop()
"""

#lambda funkce
"""
soucet=lambda a,b:a+b
print(soucet(2,3))
"""
from tkinter import *
import random as rnd

def Mocnina(x):
    vystup["text"]="{}^2 = {}".format(x,x**2)

hlavni=Tk()

m1=Button(hlavni,text="Mocnina malého \nčísla",width=15,command=lambda:Mocnina(rnd.randint(1,10)))
m1.grid(padx=5,pady=5)

m2=Button(hlavni,text="Mocnina velkého \nčísla",width=15,command=lambda:Mocnina(rnd.randint(10,100)))
m2.grid(row=0,column=1,padx=5,pady=5)

vystup=Label(hlavni,text="Mocnina",font="Arial 10 bold")
vystup.grid(row=1,column=0,columnspan=2,pady=5)


hlavni.mainloop()


















