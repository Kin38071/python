# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:15:36 2020

@author: Jan
"""
#1
n=int(input("Zadejde mocninu: "))
for i in range(0,21,2):
    print(str(i)+"^"+str(n)+"=",i**n)
#2
pocet=int(input("Zadejte počet zaměstnanců: "))
mzda=0
celkem=0
pod=0
for i in range(pocet):
    mzda=int(input("Zadejte mzdu zaměstnance: "))
    celkem=celkem+mzda
    if mzda<10000:
        pod=pod+1
prumer=celkem/pocet
print("Průměrná mzda: ",prumer)
print("Počet mezd pod 10 000: ",pod)
#3
N=int(input("Zadejte hodnotu: "))
for i in range(N):
    for j in range(1,N-i+1):
        print("*",end="")
    print()
#4
print("Dokonalá čísla menší než 1000: ")
for i in range(1,1001):
    vys=0
    for j in range(1,i):
        if i%j==0:
            vys=vys+j
    if i==vys:
        print(i,end=",")