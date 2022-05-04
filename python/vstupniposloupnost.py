# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:41:04 2020

@author: Jan
"""
import random
"""
#Vstupní posloupnost N čísel
#Průměrný měsíční plat zaměstnance
soucet=0
for i in range(12):
    plat=int(input("Zadej příjem za "+str(i+1)+". měsíc: ")) #str převádí číslo na textový řetězec
    soucet=soucet+plat #soucet+=plat
print("Průměrný plat zaměstnance: ",round(soucet/12))

#počet čísel dělitelných 3 (ve vsutpní posloupnostiN čísel)
pocet=int(input("Zadej počet čísel: "))
pocet3=0
for i in range(1,pocet+1):
    cislo=int(input("Zadej "+str(i)+". číslo: "))
    if cislo%3==0:
        pocet3=pocet3+1 #pocet3+=1
print("Počet čísel dělitelných 3: ",pocet3)
"""
#počet a průměr kladných a záporných z N náhodnýhc čísel od -100 do 100
n=int(input("Zadej počet čísel: "))
soucetK=0
pocetK=0
soucetZ=0
pocetZ=0
for i in range(n):
    cislo=random.randint(-100,100)
    if cislo>0:
        soucetK+=cislo
        pocetK+=1
    elif cislo<0:
        soucetZ+=cislo
        pocetZ+=1
print("Počet kladných: ",pocetK)
print("Průměr kladných: ",soucetK/pocetK)
print("Počet záporných: ",pocetZ)
print("Průměr záporných: ",soucetZ/pocetZ)