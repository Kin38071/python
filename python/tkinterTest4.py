# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 08:09:20 2022

@author: kin38071
"""
from tkinter import *
import math

def Cosx():
    for i in range(0,12,2):
        zahl[i]["text"]="x(°)"
    for i in range(1,12,2):
        zahl[i]["text"]="cos(x)"
    for i in range(1,11):
        sez[i-1]["text"]=str(i)
        sez[i+10-1]["text"]=str(round(math.cos(math.radians(i)),5))
        sez[i+20-1]["text"]=str(i+10)
        sez[i+30-1]["text"]="{}".format(round(math.cos(math.radians(i+10)),5))
        sez[i+40-1]["text"]=str(i+20)
        sez[i+50-1]["text"]="{}".format(round(math.cos(math.radians(i+20)),5))
        sez[i+60-1]["text"]=str(i+30)
        sez[i+70-1]["text"]="{}".format(round(math.cos(math.radians(i+30)),5))
        sez[i+80-1]["text"]=str(i+40)
        sez[i+90-1]["text"]="{}".format(round(math.cos(math.radians(i+40)),5))
        sez[i+100-1]["text"]=str(i+50)
        sez[i+110-1]["text"]="{}".format(round(math.cos(math.radians(i+50)),5))

def Tgx():
    for i in range(0,12,2):
        zahl[i]["text"]="x(°)"
    for i in range(1,12,2):
        zahl[i]["text"]="tg(x)"
    for i in range(1,11):
        sez[i-1]["text"]=str(i)
        sez[i+10-1]["text"]=str(round(math.tan(math.radians(i)),5))
        sez[i+20-1]["text"]=str(i+10)
        sez[i+30-1]["text"]="{}".format(round(math.tan(math.radians(i+10)),5))
        sez[i+40-1]["text"]=str(i+20)
        sez[i+50-1]["text"]="{}".format(round(math.tan(math.radians(i+20)),5))
        sez[i+60-1]["text"]=str(i+30)
        sez[i+70-1]["text"]="{}".format(round(math.tan(math.radians(i+30)),5))
        sez[i+80-1]["text"]=str(i+40)
        sez[i+90-1]["text"]="{}".format(round(math.tan(math.radians(i+40)),5))
        sez[i+100-1]["text"]=str(i+50)
        sez[i+110-1]["text"]="{}".format(round(math.tan(math.radians(i+50)),5))

hlavni=Tk()
hlavni.title("Tabulka goniometrických funkcí")
zahl=[]
sez=[]

for i in range(12):
    e=Button(hlavni,width=10)
    zahl.append(e)
    e.grid(row=0,column=i)
    zahl[i]["bg"]="purple"

for i in range(12):
    for j in range(1,11):
            e=Button(hlavni,width=10)
            sez.append(e)
            e.grid(row=j,column=i)

ram=LabelFrame(hlavni,text="Výběr funkce")
ram.grid(row=12,column=0,columnspan=15)
prvni=Button(ram,width=15,text="cos(x)", command=Cosx)
prvni.grid(row=0,column=0,padx=5,pady=5)
druhe=Button(ram,width=15,text="tg(x)", command=Tgx)
druhe.grid(row=0,column=1,padx=5,pady=5)

hlavni.mainloop()