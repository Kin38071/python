# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:37:27 2021

@author: Jan
"""
import random
#1
print("1.")
seznam=[]
for i in range(20):
    x=random.randint(-10000,10000)
    seznam.append(x)
print(seznam)
seznam.sort()
print(seznam)
#2
print("2.")
seznam=[]
seznam2=[]
for i in range(10):
    x=random.randint(1,100)
    seznam.append(x)
seznam.sort()
for i in seznam:
    y=i**2
    seznam2.append(y)
print(seznam)
print(seznam2)
#3
print("3.")
seznamL=[]
for i in seznam2:
    if i%2!=0:
        seznamL.append(i)
print(seznamL)
#4
print("4.")
x=seznam2.count(81)
print(x)
for i in range(10):
    if seznam2.count(81)>0:
        seznam2.remove(81)
print(seznam2)