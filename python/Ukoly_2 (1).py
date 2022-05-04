# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:51:08 2020

@author: kin38071
"""
import math
#1
R=float(input("Zadej poloměr koule: "))
povrch=4*math.pi*R**2
objem=(4/3)*math.pi*R**3
print("Povrch je: ",povrch)
print("Objem je: ",objem)
#2
F=float(input("Zadej číslo: "))
fakt=math.factorial(F)
print("Faktoriál čísla je: ",fakt)
#3
a=float(input("Zadej číslo A: "))
b=float(input("Zadej číslo B: "))
c=float(input("Zadej číslo C: "))
D=b**2-(4*a*c)
Xa=(-b+math.sqrt(D))/2*a
Xb=(-b-math.sqrt(D))/2*a
print("X1 je: ",Xa)
print("X2 je: ",Xb)
#4
uhel=float(input("Zadej velikost úhlu v stupních: "))
uhelrad=math.radians(uhel)
sin=math.sin(uhelrad)
cos=math.cos(uhelrad)
print("Sinus úhlu je: ",sin)
print("Cosinus úhlu je: ",cos)