# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 12:49:31 2021

@author: Jan
"""
#1
x=1
while x<=10:
    print(x,"^2 =",x**2)
    print(x,"^3 =",x**3)
    x=x+0.5
#2
x=1
y=1
while y!=0.01:
    x=x+1
    y=1/x
    print("1/",x,"=",y)
#3
delka=int(input("Zadejte délku spoření v letech: "))
vklad=int(input("Zadejde hodnotu měsíčního vkladu: "))
urok=float(input("Zadejte výšku úroku: "))
celkem=0
doba=0
u=0
c=0
delkam=delka*12
while doba<delkam:
    doba=doba+1
    celkem=celkem+vklad
    u=(celkem/100)*urok
    c=celkem+u
print("Naspořená částka =",c)
