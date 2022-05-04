# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:20:22 2020

@author: Jan
"""
import random
#1
N=int(input("Zadejte počet čísel: "))
soucet=0
for i in range(1,N+1):
    soucet=soucet+i
print("součet čísel =",soucet)
#2
N=int(input("Zadejte počet čísel: "))
suda=0
licha=0
soucetS=0
soucetL=0
for i in range(N):
    cislo=random.randint(1,100)
    if cislo%2==0:
        suda=suda+1
        soucetS=soucetS+cislo
    else:
        licha=licha+1
        soucetL=soucetL+cislo
print("Počet sudých: ",suda)
print("Průměr sudých: ",soucetS/suda)
print("Počet lichých: ",licha)
print("Průměr lichých: ",soucetL/licha)
#3
tridy=int(input("Zadejte počet tříd ve škole: "))
zaci=0
prumer=0
for i in range(tridy):
    zaci=int(input("Zadejte počet žáků v "+str(i+1)+". třídě: "))
    prumer=prumer+zaci
print("Průměrný počet žáků ve třídě je: ",round(prumer/tridy))
#4
N=int(input("Zadejte počet čísel: "))
nejvetsi=0
for i in range(N):
    cislo=int(input("Zadejte číslo: "))
    if cislo>nejvetsi:
        nejvetsi=cislo
print("Největší číslo je",nejvetsi)