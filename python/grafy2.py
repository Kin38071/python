# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:45:55 2021

@author: Jan
"""
from pylab import *

#Zobrazení více grafů - v samostatných oknech - figure
"""
x=arange(0,10,0.2)
y1=x**2
y2=x**3
#figure(1)              #nyní budeme kreslit do okna 1
figure("první")
plot(x,y1)
plot(x,y2)
grid(True)
figure(2)           #nyní budeme kreslit do okna 2
plot(y1,x)
show()
"""
#Zobrazení více samostatných grafů v jednom okně - subplot(početřádků,početsloupců,číslografu)
"""
x1=arange(1,4*pi,0.2)
x2=arange(0,10,0.2)
y1=sin(x1)
y2=cos(x1)
y3=x2**2
y4=x2**3

subplot(2,2,1)
plot(x1,y1,linewidth=3)
grid(True)


subplot(2,2,2)
plot(x1,y2,"b--")

subplot(2,2,3)
plot(x2,y3,label="x^2")
legend(loc="best")
grid(True)

subplot(2,2,4)
plot(x2,y4)
grid(True)

show()
"""
#Vyplnění plochy pod grafem - fill()
"""
x=arange(1,3*pi,0.01)
y=sin(x)

fill(x,y,"#00ff42")
plot(x,y,linewidth=3)
grid(True)
xlim(1,3*pi)

show()
"""
#Vyplnění plochy mezi grafy
#fill_between(x,y1,y2,where=podmínka,parametry)
"""
x=arange(1,3*pi,0.01)
y1=sin(x)
y2=cos(x)
fill_between(x,y1,y2,facecolor="gray")
plot(x,y1)
plot(x,y2)
grid(True)
xlim(1,3*pi)

show()
"""
x=arange(1,3*pi,0.01)
y1=sin(x)
y2=cos(x)

#fill_between(x,y1,y2,where=y2>y1,facecolor="magenta")
#fill_between(x,y1,y2,where=y1>y2,facecolor="purple")
fill_between(x,y1,facecolor="lightblue")    #plocha mezi fcí a osou x
plot(x,y1)
plot(x,y2)
grid(True)
xlim(1,3*pi)

show()