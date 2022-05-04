# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:33:26 2020

@author: Jan
"""
import random

#1
x=int(input("Zadejte číslo: "))
print("Malá násobilka čísla",x,":")
for i in range(1,11):
    z=x*i
    print(i,"*",x,"=",z)
#2
print("Druhé mocniny čísel od 1 do 10:")
for i in range(1,11):
    x=i**2
    print(i,"^",2,"=",x)
#3
N=int(input("Zadejte číslo: "))
n=N+1
x=0
for i in range(1,n):
    x=x+i
print("Součet celých čísel od 1 do",N,"=",x)
#4
A=int(input("Zadejte číslo A: "))
B=int(input("Zadejte číslo B: "))
b=B+1
x=0
for i in range(A,b):
    if i%3==0:
        x=x+1
print("Mezi čísly",A,"až",B,"je",x,"čísel dělitelných 3")
#5
x=int(input("Zadejte číslo: "))
y=x+1
print("Dělitele čísla",x,"jsou:")
for i in range(1,y):
    if x%i==0:
        print(i)
#6
x=int(input("Zadejte, kolikrát chcete hodit kostkou: "))
x=x+1
for i in range(1,x):
    y=random.randint(1,6)
    print(i,":","kostka hodila",y)
#7
x=int(input("Zadejte číslo: "))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print("Dané číslo není prvočíslo")
            break
    else:
        print("Dané číslo je prvočíslo")
else:
    print("Dané číslo není prvočíslo")