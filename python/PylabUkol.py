# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:14:47 2021

@author: Jan
"""
from pylab import *
import random
#1
x=arange(0,10.1,0.5)
y=(x**3)-(2*(x**2))+x-1
plot(x,y,"r",linewidth=5)
plot(x,y,"ko")
grid(True)
xlim(0,10)
show()
#2
hodnotyx=[]
hodnotyy=[]
for i in range(20):
    x=random.randint(0,100)
    y=random.randint(0,100)
    hodnotyx.append(x)
    hodnotyy.append(y)
x=array(hodnotyx)
y=array(hodnotyy)
plot(x,y,"ks")
xlim(0,100)
ylim(0,100)
grid(True)
show()
#3
xmin=int(input("Zadejte minimální hodnotu x: "))
xmax=int(input("Zadejte maximální hodnotu x: "))
x=linspace(xmin,xmax,50)
y=2/(x+1)
plot(x,y,"b--",linewidth=3,label="y=2/(x+1)")
xlim(xmin,xmax)
xlabel("osa x")
ylabel("osa y")
grid(True)
legend(loc="best")
show()
#4
seznamx=[]
seznamy=[]
xmax=-1
ymax=-1
print("Zadávejte pouze kladné hodnoty")
for i in range(3):
    x=int(input("Zadejte hodnotu x bodu: "))
    if x>xmax:
        xmax=x
    if x<0:
        print("Zadávejte pouze kladné hodnoty")
        break
    y=int(input("Zadejte hodnotu y bodu: "))
    if y>ymax:
        ymax=y
    if y<0:
        print("Zadávejte pouze kladné hodnoty")
        break
    seznamx.append(x)
    seznamy.append(y)
vekx=array(seznamx)
veky=array(seznamy)
xlim(0,xmax+1)
ylim(0,ymax+1)
plot(vekx,veky,"r^")
show()