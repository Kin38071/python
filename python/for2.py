# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:55:37 2020

@author: Jan
"""
#for - práce s řetězci
"""
for i in "Olomouc":
    print(i)

ret=input("Zadej text: ")
for i in ret:
    print(i+"*",end="")
ret=input("Zadej text: ")
for i in ret:
    print(i)
    if i=="a":
        print("Našel jsem písmeno a")
"""
#Vnořené cykly
"""
n=10
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
    
i=0
    j=0 (provedou se příkazy vnitřního cyklu)
    
*

    j=1 (a znovu)
**
    j=2 (dtto)
***
    ...
    j=9
**********

další příkaz vnější cyklu
udělá další řádek
i=1
    j=0
    j=1
......
i=9
j=9
"""
#vykreslení obdélníka
"""
x=int(input("Zadej počet znaků na řádek: "))
y=int(input("Zadej počet řádků: "))
z=input("Zadej znak: ")
for i in range(y):
    for j in range(x):
        print(z,end="")
    print()
"""
#prázdný čtverec
"""
n=10
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
#prázdný trojúhelník
n=10
for i in range(1,n+1):
    for j in range(1,n-i+1):
        if i==1 or j==1 or i+j==n:
            print("o",end="")
        else:
            print(" ",end="")
    print()
