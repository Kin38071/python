# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:21:58 2021

@author: Jan
"""

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