# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:28:21 2021

@author: Jan
"""
"""
#seznamy - pokračování
#vyhledávání nejmenšího/největšího čísla
from random import *

cisla=[]
pocet=int(input("Zadej počet čísel: "))
for i in range(pocet):
    c=randint(-100,100)
    cisla.append(c)
print(cisla)

m=cisla[0]
poz_m=0
for i in cisla:
    if i<m:
        m=i
        poz_m=cisla.index(i)
        
print("Nejmenší je:",m)
print("Jeho pozice v seznamu:",poz_m+1)

#Převedení řetězce na seznam
ret=input("zadejte text: ")

pismena=list(ret)
print(pismena)

pismena=[]
for i in ret:
    if i!=" ":
        pismena.append(i)
print(pismena)

pismena.sort()
print(pismena)

ret=""
for i in pismena:
    ret=ret+i
print(ret)

#statistika písmen
abeceda="abcdefghijklmnopqrstuvwxyz"
ret=input("Zadej text: ")

ret=ret.lower()
seznam=list(ret)
for i in abeceda:
    if i in seznam:
        print(i,":",seznam.count(i))    #jen písmena, která tam jsou
        
for i in abeceda:                       #celá abeceda
    print(i,":",seznam.count(i))
"""
#Metoda split() - dělí řetězec na části do seznamu
ret="Toto je (krátký) text"
print(ret.split())  #oddělovačem jsou bílé znaky

print(ret.split("("))   #jiný oddělovač než předdefinovaný

datum="12.3.2021"
seznam=datum.split(".")
print("Den:",seznam[0])
print("Měsíc:",seznam[1])
print("Rok:",seznam[2])