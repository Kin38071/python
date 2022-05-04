# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:34:04 2021

@author: Jan
"""
import math
print("***** MENU *****")
print("1 = KRYCHLE")
print("2 = KVADR")
print("3 = KOULE")
print("4 = VALEC")
print("cokoliv jiného = konec programu")
volba=1
while volba<5:
    volba=int(input("Zadejte číslo: "))
    if volba==1:
        a=float(input("Zadejte délku a: "))
        S=6*(a**2)
        V=a**3
        print()
        print("S =",round(S,5))
        print("V =",round(V,5))
        continue
    elif volba==2:
        a=float(input("Zadejte délku a: "))
        b=float(input("Zadejte délku b: "))
        c=float(input("Zadejte délku c: "))
        S=2*((a*b)+(b*c)+(a*c))
        V=a*b*c
        print()
        print("S =",round(S,5))
        print("V =",round(V,5))
        continue
    elif volba==3:
        r=float(input("Zadejte velikost r: "))
        S=4*math.pi*(r**2)
        V=(4/3)*math.pi*(r**3)
        print()
        print("S =",round(S,5))
        print("V =",round(V,5))
        continue
    elif volba==4:
        r=float(input("Zadejte velikost r: "))
        v=float(input("Zadejte velikost v: "))
        S=(2*math.pi*(r**2))+(2*math.pi*r*v)
        V=math.pi*(r**2)*v
        print()
        print("S =",round(S,5))
        print("V =",round(V,5))
        continue
    else:
        break