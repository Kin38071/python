# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:06:34 2021

@author: kin38071
"""
import random
#1
a=float(input("Zadejte hodnotu a: "))
b=float(input("Zadejte hodnotu b: "))
c=float(input("Zadejte hodnotu c: "))
if a==0 and b>0:
    x=(-c)/b
    print("Rovnice je lineární, x =",x)
if a==0 and b==0 and c==0:
    print("Rovnice je lineární, má nekonečně mnoho řešení")
if a==0 and b==0 and c>0:
    print("Rovnice je lineární, nemá řešení")
if a>0:
    D=b**2-(4*a*c)
    if D>0:
        x1=(-b+(D**1/2))/2*a
        x2=(-b-(D**1/2))/2*a
        print("Rovnice má dvě řešení, x1 =",x1,"x2 =",x2)
    if D==0:
        x=-b/(2*a)
        print("Rovnice má jedno řešení, x =",x)
    if D<0:
        print("Rovnice nemá řešení v oboru R")
#2
x=int(input("Zadejte první číslo: "))
y=int(input("Zadejte druhé číslo: "))
z=int(input("Zadejte třetí číslo: "))
seznam=[]
seznam.append(x)
seznam.append(y)
seznam.append(z)
seznam.sort()
print("min =",seznam[0],"str =",seznam[1],"max =",seznam[2])
#3
n=int(input("Zadejte mocninu: "))
for i in range(0,21,2):
    print(str(i)+"^"+str(n),"=",i**n)

#4
pocet=int(input("Zadejte počet zaměstnanců: "))
mzdycelkem=0
pod=0
for i in range(pocet):
    x=int(input("Zadejte mzdu: "))
    mzdycelkem=mzdycelkem+x
    if x<10000:
        pod=pod+1
prumer=mzdycelkem/pocet
print("Průměrná mzda: ",prumer)
print("Počet mezd pod 10000: ",pod)

#5
print()
cislo=random.randint(100,100001)
print("Vygeneroval jsem číslo",cislo)
soucet=0
while cislo>0:
    p=cislo%10
    soucet=soucet+p
    cislo=cislo//10
print("Jeho ciferný součet je",soucet)