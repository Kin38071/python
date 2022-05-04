# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:10:32 2021

@author: Jan
"""
"""
#Seznamy - list - []
#Vytvoření seznamu a základní manipulace s nimi

seznam=[]     #prázdný seznam
print(seznam)

seznam=[3,"text",5.0]
print(seznam)

seznam2=seznam+seznam     #sčítání
print(seznam2)

seznam3=seznam*3          #násobení celým číslem
print(seznam3)

print(seznam[0])          #výpis prvního prvku

seznam[2]="Pátek"         #přiřazení do seznamu
print(seznam)

seznam=[0,1,2,3,4,5,6,7,8,9]
print(seznam[:4])         #první 4
print(seznam[4:])         #bez prvních 4
print(seznam[-4:])        #poslení 4
print(seznam[1:4])        #od indexu 1 po 4 celkem
print(seznam[1:6:2])      #od indexu 1 po 5 celkem každý druhý

#operace se seznamy
ovoce=["jablka","hrušky","třešně"]
print(ovoce)

#přidání do seznamu
ovoce.append("maliny")
print(ovoce)

ovoce=ovoce+["višně"]
print(ovoce)

#vložení do seznamu
ovoce.insert(0,"meruňky")
print(ovoce)

#mazání ze seznamu
ovoce.pop(1)              #ovoce.pop() - odebere z konce seznamu
print(ovoce)

#zjištení existence prvku v seznamu (četnost)
x=ovoce.count("maliny")
print(x)

#odebrání konkrétního prvku (jen první výskyt)
ovoce.remove("višně")
print(ovoce)

if ovoce.count("jahody")>0:
    ovoce.remove("jahody")
print(ovoce)

#seřazení seznamu
ovoce.sort()
print(ovoce)

#obrácení seznamu
ovoce.reverse()
print(ovoce)

#délka seznamu
print(len(ovoce))

#Procházení seznamu
ovoce=["jablka","hrušky","třešně"]
for i in ovoce:
    print("Mé oblíbené ovoce je",i)
    x=ovoce.index(i)
    print("V seznamu je na",x+1,". místě")
"""
#Vzorový příklad
#načti 5 čísel a přidáme je do seznamu
seznam=[]
for i in range(5):
    x=int(input("Zadej číslo: "))
    seznam.append(x)
print(seznam)

#z toho seznamu vytvoříme nový, který bude obsahovat dvojnásobky čísel
seznam2=[]
for i in seznam:
    seznam2.append(i*2)
print(seznam2)

#z prvního seznamu vytvoříme seznam poze kladých čísel
seznamK=[]
for i in seznam:
    if i>0:
        seznamK.append(i)
print(seznamK)