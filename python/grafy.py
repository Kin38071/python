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
"""
x=arange(5)
print(2*x)
print(x+10)
print((2*x+10)/4)
print(sin(x))
print(sqrt(x))
"""
#seznam vs vektor
"""
seznam=[5,4,7.6]
print(seznam*3)
vektor=array(seznam)
print(vektor*3)
"""
#Vykreslení grafu
"""
x=arange(0,6.5,0.1)
y=sin(x)
plot(x,y)       #vykreslí graf
grid(True)      #mřížka
title("Graf funkce sin(x)")     #titulek
xlabel("Osa x")     #popis osy x
ylabel("Osa y")     #popis osy y

show()          #zobrazí okno s grafem na obrazovce
"""
#Nastavení typů čar
"""
x=linspace(-10,10,40)
y1=2*x+1
y2=x**2
y3=x**3
#plot(x,y1,x,y3)
#plot(x,y1,"c--",linewidth=3)
plot(x,y1,"r")
plot(x,y1,"bo")
plot(x,y2,"ks")
plot(x,y3,"k^")

show()
"""
#Zobrazení legendy
x=arange(0,10,0.2)
y1=x**2
y2=x**3
plot(x,y1,"b:",label="y1=x**2")
plot(x,y2,"k--",label="y2=x**3")
grid(True)
legend(loc="best")
xlim(0,7)       #rozsah osy x
#ylim(0,1000)   #rozsah osy y

show()