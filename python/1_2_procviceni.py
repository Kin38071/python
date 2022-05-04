# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:51:17 2020

@author: kin38071
"""
import math
#1
prepona=float(input("Zadej délku přepony: "))
druhodvesna=float(input("Zadej délku druhé odvěsny: "))
prvodvesna=math.sqrt(prepona**2-druhodvesna**2)
print("Délka odvěsny =",prvodvesna)
#2
a=float(input("Zadej délku strany A: "))
b=float(input("Zadej délku strany B: "))
c=float(input("Zadej délku strany C: "))
print("Objem = ",a*b*c)
print("Povrch = ",2*a*b+2*b*c+2*a*c)
#3
mm=float(input("Zadej velikost v mm: "))
metry=mm//1000
centimetry=mm%1000//10
milimetry=mm%1000//100
print(mm,"mm =",metry,"m,",centimetry,"cm a",milimetry,"mm.")
#4
trojA=float(input("Zadej délku strany A: "))
trojB=float(input("Zadej délku strany B: "))
trojC=float(input("Zadej délku strany C: "))
trojobvod=trojA+trojB+trojC
trojS=trojobvod/2
trojobsah=math.sqrt(trojS*(trojS-trojA)*(trojS-trojB)*(trojS-trojC))
trojobsahvypsat=round(trojobsah, 2)
print("Trojúhelník o stranách délky",trojA,"cm,",trojB,"cm a",trojC,"cm má obvod",trojobvod,"cm a obsah",trojobsah,"cm^2.")
#5
d=float(input("Zadej první číslo: "))
e=float(input("Zadej druhé číslo: "))
f=float(input("Zadej třetí číslo: "))
g=float(input("Zadej čtvrté číslo: "))
h=float(input("Zadej páté číslo: "))
souc=float(d+e+f+g+h)
print("Součet = ",souc)
print("Průměr = ",souc/5)
#6
hruba=float(input("Zadejte výši hrubé měsíční mzdy zaměstnance: "))
zaloha=float(input("Zadejte částku, která byla zaměstnanci vyplacena jako záloha: "))
dan=hruba/100*15
zdravotni=hruba/100*6
socialni=hruba/100*13
vyplaceno=hruba-zaloha-dan-zdravotni-socialni
print("z hrubé mzdy činí daň",dan,", zdravotní pojištění",zdravotni," a sociální pojištění",socialni)
print("zaměnstanci bude vyplaceno: ",vyplaceno)
