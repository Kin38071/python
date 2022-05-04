# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 09:12:38 2021

@author: Jan
"""
#Pylab - grafy
#vytvoření vektoru
#a) ze seznamu

from pylab import *
"""
seznam=[5,4,37.4,7.9]
vektor1=array(seznam)
print(vektor1)
vektor2=array([10,9,12])
print(vektor2)
"""
#b) jako posloupnost
"""
v1=arange(5)
print(v1)
v2=arange(10,18)
print(v2)
v3=arange(2.7,4.5,0.1)
print(v3)
"""
#c) jako rozsah s počtem hodnot
"""
x=linspace(0,10,50)         #dolní mez, horní mez, počet hodnot
print(x)
"""
#operace s vektory
x=arange(5)
print(2*x)
print(x+10)
print((2*x+10)/4)
print(sin(x))