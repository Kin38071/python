# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:50:00 2022

@author: narut
"""

from tkinter import *
from datetime import *
import random

def Zmena():
    barva ="#"+"%06x" % random.randint(0, 0xFFFFFF)
    hlavni["bg"]=barva
    hlavni.after(1000,Zmena)
    
    
def Aktualizace():
    ted=datetime.now()
    cas["text"]="{:2}:{:2}:{:2}".format(ted.hour,ted.minute,ted.second)
    hlavni.after(100,Aktualizace)

#1

hlavni=Tk()

Zmena()

hlavni.mainloop()

#2

hlavni=Tk()

cas=Label(hlavni,text="00:00:00")
cas.pack(padx=10,pady=10)

Aktualizace()




hlavni.mainloop()