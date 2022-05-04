# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:45:09 2021

@author: Jan
"""
import random
#1
p=0
v=0
N=int(input("Zadejte číslo: "))
while p<N:
    p=p+1
    if p%2==0:
        v=p**2
        if v<N:
            print(str(p)+"^2 =",v)
#2
x=random.randint(100,100000)
print("Vygeneroval jsem číslo",x)
v=0
while x>0:
    v=v+x%10
    x=x//10
print("Jeho ciferný součet je",v)
#3
c=int(input("Zadejte celkovou půjčenou částku: "))
m=int(input("Zadejte hodnotu měsíční splátky: "))
u=int(input("Zadejte úrok v %: "))
mes=0
uc=c+((c/100)*u)
while uc>0:
    uc=uc-m
    mes=mes+1
rok=mes//12
mes=mes%12
print(rok,"let a",mes,"měsíců")