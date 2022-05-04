# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:46:23 2021

@author: Jan
"""

#příkazy řízení cyklu
#continue - způsobí ukončení akutálního opakování, zbytek cyklu se neprovede,
#ale cyklus pokačuje následujícím opakováním
#break - ukončení cyklu
"""#
for i in range(1,200):
    if i%3==0:
        print("asd")
        continue
    if i>20:
        print("konec")
        break
    print(i)
#
c=10
while c>0:
    print(c)
    c=c-1
    if c==5:
        break
print("konec")
#
c=10
while c>0:
    c=c-1
    if c==5:
        continue
    print(c)
print("konec")
#
import random

x=1
while x!=10:
    x=random.randint(2,20)
    if x%2==0:
        continue
    print(x)
    if x==5:
        break
"""#
#nekonečný cyklus
k=10
while True:
    cislo=int(input("Zadejte číslo: "))
    print(cislo)
    if cislo!=k:
        print("vedle")
    else:
        print("Trefa!")
        break