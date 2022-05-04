"""
#a) Vytvoření okna
from tkinter import *   

hlavni=Tk()

hlavni.mainloop()


#b) Nastavení vlastností okna
from tkinter import *   

hlavni=Tk()
hlavni.title("pokus")        #titulek
hlavni.configure(width=300,height=200,bg="navy") #šířka, výška, barva
#hlavni.minsize(200,100)      #minimální velikost
#hlavni.maxsize(400,200)      #maximální velikost
#hlavni.resizable(FALSE,FALSE)#zákaz změny velikosti okna
#v tomto případě nastavujeme jen width a height, nebo minsize

hlavni.mainloop()


#c) Komponenta Label - popis jiných komponent, jednoduchý výstup
from tkinter import *   

hlavni=Tk()

stitek=Label(hlavni,text="Ahoj")
#identifikator=komponenta(rodičovská komponenta,zobrazený text)
stitek.pack()
#umístění komponenty do okna

hlavni.mainloop()


#d) Label - vlastnosti
from tkinter import *   

hlavni=Tk()

stitek=Label(hlavni,text="Ahoj",font="Arial 12",fg="blue",bg="lightblue")
#typ písma a jeho velikost, barva písma, barva pozadí
stitek.pack(padx=10,pady=10)  #"vycpávky" kolem komponenty

stitek2=Label(hlavni,text="Text",width=20,font="Tahoma 20 bold",relief="sunken")
#šířka, písmo (tučné), zvýraznění (sunken/raised/ridge/groove)
stitek2.pack(padx=10,pady=10)

s="Toto je dlouhý text pro zalomení a zarovnání"
stitek3=Label(hlavni,text=s,wraplength=100,justify="left")
stitek3.pack(padx=10,pady=10)

hlavni.mainloop()


#e) Komponenta Button - tlačítko
from tkinter import *   

hlavni=Tk()

klik=Button(hlavni,text="Akce",width=10)
klik.pack(padx=10,pady=10)

hlavni.mainloop()


#f) Připojení funkce ke komponentě
from tkinter import *   

def Klik():
    print("Kliknul jsi")

hlavni=Tk()

klik=Button(hlavni,text="Akce",width=10,command=Klik)
klik.pack(padx=10,pady=10)

hlavni.mainloop()


#g) Změna textu a barvy písma Labelu kliknutím na tlačítko a funkce pro konec
from tkinter import *   

def Zmena():
    #napis.configure(text="Něco jiného",fg="green")
    #jinak a lépe - pomocí slovníku
    napis["text"]="Jiný text"
    napis["fg"]="red"

hlavni=Tk()

napis=Label(hlavni,text="Popisek",font="Arial 15",fg="blue")
napis.pack(padx=10,pady=10)

zmena=Button(hlavni,text="Změna",width=10,command=Zmena)
zmena.pack(padx=10,pady=10)

konec=Button(hlavni,text="Konec",width=10,command=hlavni.destroy)
konec.pack(padx=10,pady=10)

hlavni.mainloop()
"""


#h) Zobrazení vypočtené hodnoty v Labelu po stisknutí tlačítka
from tkinter import *
import random as rnd

def Mocnina1():
    vystup.configure(text=str(rnd.randint(1,10)**2),fg="blue")

def Mocnina2():
    x=rnd.randint(1,10)
    vystup["text"]="{}^2 = {}".format(x,x**2)
    vystup["fg"]="green"

hlavni=Tk()

vystup=Label(hlavni,text="Výstup",font="bold",fg="white")
vystup.pack(padx=5,pady=5)

akce1=Button(hlavni,text="Mocnina",width=15,command=Mocnina1)
akce1.pack(padx=5,pady=5)

akce2=Button(hlavni,text="Mocnina jinak",width=15,command=Mocnina2)
akce2.pack(padx=5,pady=5)

hlavni.mainloop()



