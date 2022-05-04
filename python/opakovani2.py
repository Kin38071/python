# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 08:04:59 2021

@author: kin38071
"""
from pylab import *
import random
#6
cisla=[]
suda=[]
licha=[]
pocets=0
soucets=0
pocetl=0
soucetl=0
for i in range(20):
    x=random.randint(1,101)
    cisla.append(x)
    if x%2==0:
        suda.append(x)
    else:
        licha.append(x)
for i in suda:
    pocets=pocets+1
    soucets=soucets+i
prumers=soucets/pocets
for i in licha:
    pocetl=pocetl+1
    soucetl=soucetl+i
prumerl=soucetl/pocetl
print("SEZNAM ČÍSEL")
print(cisla)
print()
print("SUDÁ")
print(suda)
print("Počet sudých:",pocets)
print("Součet sudých:",soucets)
print("Průměr sudých:",prumers)
print()
print("LICHÁ")
print(licha)
print("Počet lichých:",pocetl)
print("Součet lichých:",soucetl)
print("Průměr lichých:",prumerl)
#7
x=int(input("Zadejte číslo: "))
y=bin(x)[2:]
print("Binární tvar: ",y)
#8
x=int(input("Zadejte číslo: "))
f=1
if x>0:
    for i in range(1,x+1):
        f=f*i
    print(str(x)+"! = ",f)
elif x==0:
    print("0! = 1")
else:
    print("číslo musí být kladné")

#9
print("Zadávejte pouze kladná čísla")
seznamx=[]
seznamy=[]
nejvx=0
nejvy=0
for i in range(1,4):
    x=float(input("Zadej souřadnici x"+str(i)+": "))
    if x>nejvx:
        nejvx=x
    seznamx.append(x)
    y=float(input("Zadej souřadnici y"+str(i)+": "))
    if y>nejvy:
        nejvy=y
    seznamy.append(y)
x=array(seznamx)
y=array(seznamy)
plot(x,y,"b^")
grid(True)
xlim(0,nejvx+1)
ylim(0,nejvy+1)
show()
#10
seznamx=[]
seznamy=[]
for i in range(1,6):
    x=float(input("Zadej souřadnici x"+str(i)+": "))
    seznamx.append(x)
    y=float(input("Zadej souřadnici y"+str(i)+": "))
    seznamy.append(y)
x=array(seznamx)
y=array(seznamy)
subplot(2,1,1)
plot(x,y,"r",linewidth=2)
plot(x,y,"bo")
grid(True)

x=arange(-2*pi,2*pi,0.01)
y1=sin(2*x)
y2=2*cos(x)
subplot(2,1,2)
fill_between(x,y1,y2,facecolor="lightblue")
plot(x,y1,"b")
plot(x,y2,"b")
grid(True)
xlim(-2*pi,2*pi)
show()