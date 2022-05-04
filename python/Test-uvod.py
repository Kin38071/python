# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 09:44:21 2020

@author: kin38071
"""
import math
#1
prumer=float(input("Zadej průměr válce: "))
vyska=float(input("Zadej výšku válce: "))
polomer=prumer/2
povrch=2*math.pi*polomer**2+2*math.pi*polomer*vyska
objem=math.pi*polomer**2*vyska
print("Objem válce je:",objem)
print("Povrch válce je:",povrch)
#2
A=input("Zadej název prvního předmětu: ")
a=float(input("Zadej cenu prvního předmětu: "))
B=input("Zadej název druhého předmětu: ")
b=float(input("Zadej cenu druhého předmětu: "))
C=input("Zadej název třetího předmětu: ")
c=float(input("Zadej cenu třetího předmětu: "))
cena=a+b+c
cenar=round(cena)
print("Za",A,",",B,"a",C,"jsem utratil(a) celkem",cenar,"Kč.")
#3
minuty=int(input("Zadej čas v minutách: "))
tydny=minuty//10080
dny=minuty%10080//1440
hodiny=minuty%10080%1440//60
minutyzb=minuty%10080%1440%60
print("týdny:",tydny)
print("dny:",dny)
print("hodiny:",hodiny)
print("minuty:",minutyzb)
#4
plan=int(input("Zadejte roční plán tržeb: "))
prvni=int(input("Zadejte výši tržeb za první čtvrtletí: "))
druhe=int(input("Zadejte výši tržeb za druhé čtvrtletí: "))
treti=int(input("Zadejte výši tržeb za třetí čtvrtletí: "))
ctvrte=int(input("Zadejte výši tržeb za čtvrté čtvrtletí: "))
celkem=prvni+druhe+treti+ctvrte
splneni=(100*celkem)/plan
splnenipr=round(splneni)
ctvrt=plan/4
plneni1=(100*prvni)/ctvrt
plneni1r=round(plneni1)
plneni2=(100*druhe)/ctvrt
plneni2r=round(plneni2)
plneni3=(100*treti)/ctvrt
plneni3r=round(plneni3)
plneni4=(100*ctvrte)/ctvrt
plneni4r=round(plneni4)
print("Plán se podařilo splnit na",splnenipr,"%")
print("Čtvrtletí - Plán - Skutečnost - Plnění v %")
print("1 -",ctvrt,"-",prvni,"-",plneni1r,"%")
print("2 -",ctvrt,"-",druhe,"-",plneni2r,"%")
print("3 -",ctvrt,"-",treti,"-",plneni3r,"%")
print("4 -",ctvrt,"-",ctvrte,"-",plneni4r,"%")