# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:53:26 2021

@author: Jan
"""
import random
#1
ret=input("Zadejte řetězec: ")
print("délka řetězce:",len(ret))
print("posledních 5 znaků:",ret[-5:])
#2
#a
for i in range(10):
    x=random.randint(1,1000)
    print("{0:<5}{1:5}".format(x," Kč"))
#b
for i in range(10):
    x=random.randint(1,1000)
    print("{0:>5}{1:5}".format(x," Kč"))
#c
for i in range(10):
    x=random.randint(1,1000)
    print("{0:5}{1:5}{0:5}{1:5}".format(x," Kč"))
#3
for i in range(1,11):
    print("{0:2}{1:10}".format(i,i**2))