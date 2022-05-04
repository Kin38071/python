# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:21:21 2021

@author: Jan
"""
import math

def faktor(x):
    fact=1
    if x<0:
        print("Faktoriál záporných čísel neexistuje.")
    elif x==0:
        print("1")
    else:
        for i in range(1,x+1):
            fact=fact*i
        print(str(x)+"! = ",fact)

def druhaMoc(x):
    y=x*x
    print("druhá mocnina",x,"je",y)

def tretiMoc(x):
    y=x**3
    print("třetí mocnina",x,"je",y)
    
def druhaOdmoc(x):
    if x<0:
        print("Neexistuje odmocnina záporného čísla")
    else:
        y=math.sqrt(x)
        print("druhá odmocnina",x,"je",y)
        
def prevracena(x):
    y=1/x
    print("převrácená hodnota",x,"je",y)
    
def scitani(x,y):
    z=x+y
    print(x,"+",y,"=",z)

def odcitani(x,y):
    z=x-y
    print(x,"-",y,"=",z)
    
def nasobeni(x,y):
    z=x*y
    print(x,"*",y,"=",z)
    
def deleni(x,y):
    if y==0:
        print("Nelze dělit nulou")
    else:
        z=x/y
        print(x,"/",y,"=",z)

def vklad(x):
    global ucet
    ucet=ucet+x

def vyber(x):
    global ucet
    if x>ucet:
        print("Nemáte dostatek financí na účtu")
    else:
        ucet=ucet-x
        
def stav():
    global ucet
    print(ucet)
#1
n=int(input("Zadejte číslo: "))
faktor(n)
#2
print("")
while True:
    print("1. Operace s jedním číslem")
    print("2. Operace se dvěma čísly")
    print("Cokoliv jiného = konec výběru operací")
    volba=int(input("Zadejte Vaši volbu: "))
    if volba==1:
        print("1. druhá mocnina")
        print("2. třetí mocnina")
        print("3. druhá odmocnina")
        print("4. převrácená hodnota")
        volba2=int(input("Zadejte Vaši volbu: "))
        if volba2==1:
            cislo=int(input("Zadejte číslo: "))
            druhaMoc(cislo)
            print("")
            continue
        elif volba2==2:
            cislo=int(input("Zadejte číslo: "))
            tretiMoc(cislo)
            print("")
            continue
        elif volba2==3:
            cislo=int(input("Zadejte číslo: "))
            druhaOdmoc(cislo)
            print("")
            continue
        elif volba2==4:
            cislo=int(input("Zadejte číslo: "))
            prevracena(cislo)
            print("")
            continue
        else:
            print("musíte vybrat číslo 1-4")
            print("")
            continue
    elif volba==2:
        print("1. sčítání")
        print("2. odčítání")
        print("3. násobení")
        print("4. dělení")
        volba2=int(input("Zadejte Vaši volbu: "))
        if volba2==1:
            cislo=int(input("Zadejte první číslo: "))
            cislo2=int(input("Zadejte druhé číslo: "))
            scitani(cislo,cislo2)
            print("")
            continue
        elif volba2==2:
            cislo=int(input("Zadejte první číslo: "))
            cislo2=int(input("Zadejte druhé číslo: "))
            odcitani(cislo,cislo2)
            print("")
            continue
        elif volba2==3:
            cislo=int(input("Zadejte první číslo: "))
            cislo2=int(input("Zadejte druhé číslo: "))
            nasobeni(cislo,cislo2)
            print("")
            continue
        elif volba2==4:
            cislo=int(input("Zadejte první číslo: "))
            cislo2=int(input("Zadejte druhé číslo: "))
            deleni(cislo,cislo2)
            print("")
            continue
        else:
            print("musíte vybrat číslo 1-4")
            print("")
            continue
    else:
        break
            
        
#3
print("")
ucet=int(input("Zadejte váš současný zůstatek na účtu: "))
print("1. Výběr")
print("2. Vklad")
print("3. Stav na účtu")
print("Cokoliv jiného = konec výběru operací")
while True:
    volba=int(input("Zadejte Vaši volbu: "))
    if volba==1:
        vybrat=int(input("Zadejte částku, kterou chcete z účtu vybrat: "))
        vyber(vybrat)
        continue
    elif volba==2:
        vlozit=int(input("Zadejte částku, kterou chcete na účet vložit: "))
        vklad(vlozit)
        continue
    elif volba==3:
        print("Zůstatek na Vašem účtu je",ucet)
        continue
    else:
        break