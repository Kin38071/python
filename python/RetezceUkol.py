# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:22:17 2021

@author: Jan
"""

veta="Python je skvely objektove orientovany, interpretovany a interaktivni programovaci jazyk."
#a
print("Ve větě je",len(veta),"znaků")
#b
p=0
for i in veta:
    p+=1
    if i==" " or i=="," or i==".":
        p-=1
print("Ve větě je",p,"písmen")
#c
a=0
e=0
for i in veta:
    if i=="a":
        a+=1
    if i=="e":
        e+=1
print("Ve větě je",str(a)+"x písmeno a")
print("Ve větě je",str(e)+"x písmeno e")
#d
for i in veta:
    if i=="o":
        print("python",end=" ")
print()
#e
x=veta.find("x")
if x>-1:
    print("Ve větě je písmeno \"x\"")
else:
    print("Ve větě není písmeno \"x\"")
#f
for i in range(50):
    print(veta[12],end="")
print()
#g
print(veta.replace("e","x"))
#h
print(veta.upper())