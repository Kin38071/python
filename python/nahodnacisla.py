# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:29:08 2020

@author: Jan
"""
#Náhodná čísla - knihovna random
"""
import random
import random as rnd

from random import *

randint (x,y) #generuje celá čísla ze zadaného rozsahu (x,y) včetně x a y
"""
import random
x=random.randint(10,20)
print(x)

print("Kostka hodila",random.randint(1,6))

x=random.random() #generuje náhodné číslo od 0 do 1
print(x)

x=random.uniform(10,50) #generuje náhodné R číslo kromě horní hranice
print(x)

x=random.randrange(10) #generuje náhorné R číslo od 0 do horní hranice-1 (do 9)
print(x)

x=random.randrange(0,101,2) #generuje celá čísla od 0 do 100 sudá
print(x)

x=random.choice("abcdefghi") #generuje náhodný znak ze zadaného text. řetězce
print(x)

x=random.choice(["jaro","léto","podzim","zima"]) #vybere jeden prvek ze seznamu
print(x)

x=random.sample([1,2,3,4,5,6,7],3) #generuje náhodná čísla ze seznamu (počet je dán druhým parametrem)
print(x)