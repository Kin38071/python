# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 08:04:02 2021

@author: kin38071
"""
import random
import math

def krychle(a):
    S=6*a*a
    V=a**3
    print("Povrch krychle je",S)
    print("Objem krychle je", V)
        
def kvadr(a,b,c):
    S=2*((a*b)+(b*c)+(a*c))
    V=a*b*c
    print("Povrch kvádru je",S)
    print("Objem kvádru je", V)

def koule(r):
    S=4*(math.pi)*(r**2)
    V=(4/3)*(math.pi)*(r**3)
    print("Povrch koule je",S)
    print("Objem koule je", V)
    
def valec(r,vy):
    S=(2*(math.pi)*(r**2))+(2*(math.pi)*r*vy)
    V=(math.pi)*(r**2)*vy
    print("Povrch válce je",S)
    print("Objem válce je", V)

#1

while True:
    print("")
    print("***** MENU *****")
    print("1 = KRYCHLE")
    print("2 = KVADR")
    print("3 = KOULE")
    print("4 = VALEC")
    print("cokoliv jiného = konec programu")
    vyb=int(input("Vyberte těleso: "))
    if vyb==1:
        x=int(input("Zadejte délku strany krychle: "))
        krychle(x)
        continue
    elif vyb==2:
        x=int(input("Zadejte délku strany a kvádru: "))
        y=int(input("Zadejte délku strany b kvádru: "))        
        z=int(input("Zadejte délku strany c kvádru: "))
        kvadr(x,y,z)
        continue
    elif vyb==3:
        x=int(input("Zadejte poloměr koule: "))
        koule(x)
        continue
    elif vyb==4:
        x=int(input("Zadejte poloměr válce: "))
        y=int(input("Zadejte výšku válce: "))
        valec(x,y)
        continue
    else:
        break
    
#2
gene=[]
uziv=[]
pocet=0
shoda=0
while pocet<6:
    x=random.randint(1,50)
    if x in gene:
        continue
    else:
        gene.append(x)
        pocet=pocet+1
pocet=0
while pocet<6:
    x=int(input("Zadejte číslo od 1 do 49: "))
    if x in uziv:
        print("Nezadávejte čísla, která jste již zadal.")
        continue
    elif x<1 or x>49:
        print("Zadávejte pouze čísla od 1 do 49")
        continue
    else:
        uziv.append(x)
        pocet=pocet+1
gene.sort()
uziv.sort()
for i in uziv:
    if i in gene:
        shoda=shoda+1
print("")
print("Vaše čísla:")
print(uziv)
print("Vygenerovaná čísla:")
print(gene)
print("")
print("Uhádl jste",shoda,"čísel")