# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:09:55 2020

@author: Jan
"""
import random
#1
N=int(input("Zadej číslo: "))
for i in range(1,N+1):
    for j in range(i):
        print("*",end="")
    print()
#2
N=int(input("Zadej číslo: "))
x=0
for i in range(1,N+1):
    x=random.randint(1,100)
    print(str(x)+": ",end="")
    for j in range(1,x+1):
        if x%j==0:
            print(j,"",end="")
    print()
#3
ret=input("Zadej text: ")
zna=input("Zadej znak: ")
x=0
for i in ret:
    if i==zna:
        x=x+1
print("V řetězci je",x,"krát",zna)
#4
N=int(input("Zadej číslo: "))
print("Prvočísla do",str(N)+":")
for i in range(2,N+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=",")