# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:25:28 2021

@author: Jan
"""
import random
#1
x=0
seznam=[]
for i in range(20):
    a=random.randint(1,100)
    seznam.append(a)
    if x<a:
        x=a
poz=seznam.index(x)
print(seznam)
print("Největší číslo je",x)
print("Jeho pozice je",poz+1)
#2
samoh="aeiou"
ret=input("Zadej text: ")
ret=ret.lower()
seznam=list(ret)
for i in samoh:
    print(i,":",seznam.count(i))
#3
hody=[]
for i in range(6):
    hod=random.randint(1,6)
    hody.append(hod)
postupka=[1, 2, 3, 4, 5, 6]
hody.sort()
if hody==postupka:
    print("Padla postupka!")
else:
    print("Nepadla postupka.")