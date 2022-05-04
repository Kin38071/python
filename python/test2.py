# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:42:07 2020

@author: Jan
"""
import math
import random

#1
a=float(input("Zadej hodnotu a: "))
b=float(input("Zadej hodnotu b: "))
c=float(input("Zadej hodnotu c: "))
D=(b**2)-(4*a*c)
x=(-c)/b
x1=(-b+math.sqrt(D))/2*a
x2=(-b-math.sqrt(D))/2*a
if a==0:
    print("Rovnice je lineární")
else:
    if D==0:
        print("Rovnice má jedno řešení, x=",x1)
    elif D>0:
        print("Rovnice má dvě řešení, x1 =",x1,"x2 = ",x2)
    else:
        print("Rovnice nemá řešení v oboru R")
#2
a=float(input("Zadej hodnotu a: "))
b=float(input("Zadej hodnotu b: "))
c=float(input("Zadej hodnotu c: "))
if a>c:
    a,c=c,a
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print("Trojúhelník lze sestrojit, je rovnostranný")
    elif a==b or a==c or b==c:
        print("Trojúhelník lze sestrojit, je rovnoramenný")
    else:
        print("Trojúhelník lze sestrojit, je obecný")
else:
    print("Trojúhelník nelze sestrojit")
#3
TescoC=float(input("Zadej cenu másla v Tescu: "))
TescoG=float(input("Zadej gramáž másla v Tescu: "))
GlobusC=float(input("Zadej cenu másla v Globusu: "))
GlobusG=float(input("Zadej gramáž másla v Globusu: "))
LidlC=float(input("Zadej cenu másla v Lidlu: "))
LidlG=float(input("Zadej gramáž másla v Lidlu: "))
TescoP=TescoC/TescoG
GlobusP=GlobusC/GlobusG
LidlP=LidlC/LidlG
if TescoP>GlobusP and TescoP>LidlP:
    print("Nejdražší máslo má Tesco")
if GlobusP>TescoP and GlobusP>LidlP:
    print("Nejdražší máslo má Globus")
if LidlP>TescoP and LidlP>GlobusP:
    print("Nejdražší máslo má Lidl")
if TescoP<GlobusP and TescoP<LidlP:
    print("Nejlevnější máslo má Tesco")
if GlobusP<TescoP and GlobusP<LidlP:
    print("Nejlevnější máslo má Globus")
if LidlP<TescoP and LidlP<GlobusP:
    print("Nejlevnější máslo má Lidl")
if TescoP>GlobusP and TescoP>LidlP and GlobusP<TescoP and GlobusP<LidlP:
    x=round(GlobusP/TescoP*100)
    print("Tesco má máslo dražší o",x,"%")
if TescoP>GlobusP and TescoP>LidlP and LidlP<TescoP and LidlP<GlobusP:
    x=round(LidlP/TescoP*100)
    print("Tesco má máslo dražší o",x,"%")
if GlobusP>TescoP and GlobusP>LidlP and TescoP<GlobusP and TescoP<LidlP:
    x=round(TescoP/GlobusP*100)
    print("Globus má máslo dražší o",x,"%")
if GlobusP>TescoP and GlobusP>LidlP and LidlP<TescoP and LidlP<GlobusP:
    x=round(LidlP/GlobusP*100)
    print("Globus má máslo dražší o",x,"%")
if LidlP>TescoP and LidlP>GlobusP and TescoP<GlobusP and TescoP<LidlP:
    x=round(TescoP/LidlP*100)
    print("Lidl má máslo dražší o",x,"%")
if LidlP>TescoP and LidlP>GlobusP and GlobusP<TescoP and GlobusP<LidlP:
    x=round(GlobusP/LidlP*100)
    print("Lidl má máslo dražší o",x,"%")
#4
z=int(input("Zadej číslo: "))
x=random.randint(20,50)
y=random.randint(20,50)
if x>y:
    x,y=y,x
if z<=y and z>=x:
    print("Císlo",z,"patří do intervalu <",x,",",y,">")
else:
    print("Číslo",z,"nepatří do intervalu <",x,",",y,">")