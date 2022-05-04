# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:56:38 2020

@author: Jan
"""
#1
c1=int(input("Zadej první číslo: "))
c2=int(input("Zadej druhé číslo: "))
c3=int(input("Zadej třetí číslo: "))
if c1>c3:
    c1,c3=c3,c1
if c1>c2:
    c1,c2=c2,c1
if c2>c3:
    c2,c3=c3,c2
print("Největší je",c3)
#2
a=float(input("Zadej hodnotu a: "))
b=float(input("Zadej hodnotu b: "))
if a==0 and b==0:
    print("Rovnice má nekonečně mnoho řešení.")
elif a==0:
    print("Rovnice nemá řešení.")
else:
    x=-b/a
    print("X =",x)
#3
A=float(input("Zadej hodnotu a: "))
B=float(input("Zadej hodnotu b: "))
C=float(input("Zadej hodnotu c: "))
D=(B**2)-4*A*C
if D>0:
    print("Rovnice má dva kořeny v R")
elif D<0:
    print("Rovnice nemá řešení v R")
else:
    print("Rovnice má jeden kořen v R")
#4
t1=float(input("Zadej první hodnotu: "))
t2=float(input("Zadej druhou hodnotu: "))
t3=float(input("Zadej třetí hodnotu: "))
if t1>t3:
    t1,t3=t3,t1
if t1>t2:
    t1,t2=t2,t1
if t2>t3:
    t2,t3=t3,t2
if t1+t2>t3 and t1+t3>t2 and t2+t3>t1:
    if t3**2==t1**2+t2**2:
        print("Lze sestrojit, je pravoúhlý")
    else:
        print("Lze sestrojit, není pravoúhlý")
else:
    print("Nelze sestrojit")
#5
rok=int(input("Zadej číslo roku: "))
x=rok%4
if x==0:
    print("Letos je přestupný rok.")
elif x==1:
    print("Přestupný rok byl loni.")
elif x==2:
    print("Přestupný rok bude za 2 roky.")
elif x==3:
    print("Přestupný rok bude za rok.")