# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:01:05 2022

@author: narut
"""

from tkinter import *

#text
"""
def Smazat():
    text.delete(1.0,END)     #smaže vše
    text.focus_set()         #nastaví kurzor do komponenty
    #text.delete(1.0,2.0)    #smaže první řádek
    #text.delete(2.0,END)    #od druhého do konce
    #text.delete(INSERT,END) #od místa kurzoru na konec
    #text.delete(INSERT)     #znak vpravo od kurzoru


def Precist():
    ret=text.get(1.0,END)
    print(ret)

hlavni=Tk()

text=Text(hlavni,font="Arial 10")
text.pack()

#vložení textu
text.insert(END,"ahoj")
text.insert(1.0,"Karle")    #první řádek, nultý znak 
                            # INSERT - místo kurzoru
#vložení textu se stylem
text.tag_config("modre",font="20",foreground="blue",underline=1)
text.insert(END,"\n")
text.insert(END,"ahoj","modre")
text.insert(END," světe")

text.insert(END,"\n")
text.insert(END,"Ahoj, světe","cervene")
text.tag_config("cervene",foreground="red",font="Arial 20 bold")


smazat=Button(hlavni,text="Smazat",width=10,command=Smazat)
smazat.pack(padx=5,pady=5,side=LEFT)

precist=Button(hlavni,text="Přečíst",width=10,command=Precist)
precist.pack(padx=5,pady=5,side=LEFT)

hlavni.mainloop()
"""

#Datum a čas

from datetime import *
"""
dnes=datetime.now()
print(str(dnes))

print("Rok: {:d}".format(dnes.year))
print("Měsíc: {:02d}".format(dnes.month))
print("Den: {:02d}".format(dnes.day))
print("Hodina: {:02d}".format(dnes.hour))
print("Minuta: {:02d}".format(dnes.minute))
print("Sekunda: {:02d}".format(dnes.second))
print("Mikrosekunda: {:d}".format(dnes.microsecond))
"""
#Časovač - after (provedení událoszi každých n milisekund)
#okno.after(čas,událost)

hlavni=Tk()

def Vypis():
    print("Proběhl výpis")
    dnes=datetime.now()
    text.delete(1.0,END)
    text.insert(END,"Čas: {:02d}".format(dnes.second))
    hlavni.after(1000,Vypis)

text=Text(hlavni,font="Arial 20")
text.pack()

Vypis()














hlavni.mainloop()