# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:13:20 2021

@author: Jan
"""
import math
#1
def Prepona(a,b):
    c=math.sqrt((a**2)+(b**2))
    return c
#2
def Mocnina(a,b):
    return a**b
#3
def Nejmensi(x,y,z):
    if x<y and x<z:
        return x
    elif y<x and y<z:
        return y
    else:
        return z

#1
prvni=int(input("Zadejte délku prní odvěsny: "))
druha=int(input("Zadejte délku druhé odvěsny: "))
print("Délka přepony:",Prepona(prvni,druha))
#2
cislo=int(input("Zadejte číslo: "))
moc=int(input("Zadejte mocninu: "))
print(str(moc)+". mocnina "+str(cislo)+" =",Mocnina(cislo,moc))
#3
prv=int(input("Zadejte první číslo: "))
druh=int(input("Zadejte druhé číslo: "))
tre=int(input("Zadejte třetí číslo: "))
print("Nejmenší číslo je: ",Nejmensi(prv,druh,tre))