#Př.1: Vytvoření jednorozměrnétabulky
from tkinter import *

hlavni=Tk()

for i in range(20):
    txt=StringVar()
    txt.set("Tlačítko "+str(i+1))
    b=Button(hlavni,textvariable=txt)
    b.pack(fill=X)
        
hlavni.mainloop()

#Př.2: Vytvoření tabulky s přístupem k jednotlivým komponentám
from tkinter import *

hlavni=Tk()

sez=[]

for i in range(20):
    txt=StringVar()
    txt.set("Tlačítko "+str(i+1))
    b=Button(hlavni,textvariable=txt)
    sez.append(b)      #komponenty přidáme do seznamu
    #přes indexy seznamu můžeme ke komponentám přistupovat
    if i%2==0:
        sez[i]["bg"]="red"
    else:
        sez[i]["bg"]="blue"
    b.pack(fill=X)

#zakázání komponenty        
sez[13]["state"]=DISABLED

hlavni.mainloop()


#Př.3: Náhodné barvy tlačítek
from tkinter import *
import random as rnd

hlavni=Tk()

sez=[]

for i in range(20):
    txt=StringVar()
    txt.set("Tlačítko "+str(i+1))
    b=Button(hlavni,textvariable=txt)
    sez.append(b)
    sez[i]["bg"]="#{:02x}{:02x}{:02x}".format(rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255))
    b.pack(fill=X)

hlavni.mainloop()


#Př.4: Dvourozměrná tabulka
from tkinter import *

hlavni=Tk()

for i in range(3):
    for j in range(10):
        txt=StringVar()
        txt.set(str(i+1)+","+str(j+1))
        b=Button(hlavni,textvariable=txt,width=10)
        b.grid(row=j,column=i)

hlavni.mainloop()

