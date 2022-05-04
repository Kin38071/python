# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:44:17 2022

@author: narut
"""

from tkinter import *
from tkinter import filedialog as fld

def Smazat():
    text.delete(1.0,END)
    text.focus_set()
    
def Ulozit():
    try:
        ret=fld.asksaveasfilename(title="Uložit soubor",defaultextension="txt")
        soubor=open(ret,"w")
        zapsat=text.get(1.0,END)
        soubor.write(zapsat)
        soubor.close()
    except:pass


def Nacist():
    try:
        ret=fld.askopenfilename()
        soubor=open(ret,"r")
        obsah=soubor.read()
        text.insert(END,obsah)
        soubor.close()
    except:pass

hlavni=Tk()

hlavniMenu = Menu(hlavni)

hlavniMenu.add_command(label="Nový", command=Smazat)
hlavniMenu.add_command(label="Otevřít", command=Nacist)
hlavniMenu.add_command(label="Uložit", command=Ulozit)


text=Text(hlavni,font="Arial 10")
text.pack()

hlavni.config(menu=hlavniMenu)

hlavni.mainloop()