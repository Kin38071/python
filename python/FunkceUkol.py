# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:39:30 2021

@author: Jan
"""
def Pricist(x):
    global cislo
    cislo=cislo+x
    print("výsledek:",cislo)

def Odecist(x):
    global cislo
    cislo=cislo-x
    print("výsledek:",cislo)
    
def Vynasobit(x):
    global cislo
    cislo=cislo*x
    print("výsledek:",cislo)
    
def Vydelit(x):
    global cislo
    cislo=cislo/x
    print("výsledek:",cislo)
    
def Pridej(jmeno):
    global evidence
    evidence.append(jmeno)

def Smaz(jmeno):
    global evidence
    evidence.remove(jmeno)

def Zjisti(jmeno):
    global evidence
    if jmeno in evidence:
        print("Zadané jméno je v evidenci.")
    else:
        print("Zadané jméno není v evidenci.")
    
def Vypis():
    global evidence
    evidence.sort
    x=1
    for i in evidence:
        print(x,i)
        x=x+1
    

#1
cislo=int(input("Zadejte číslo: "))
print("1 – PŘIČÍST")
print("2 – ODEČÍST")
print("3 – VYNÁSOBIT")
print("4 – VYDĚLIT")
print("cokoliv jiného – KONEC")
while True:
    akce=int(input("Zadejte číslo operace: "))
    if akce==1:
        y=int(input("Zadejte číslo, které má být přičteno: "))
        Pricist(y)
        continue
    elif akce==2:
        y=int(input("Zadejte číclo, které má být odečteno: "))
        Odecist(y)
        continue
    elif akce==3:
        y=int(input("Zadejte číslo, kterým má být předchozí číslo vynásobeno: "))
        Vynasobit(y)
        continue
    elif akce==4:
        y=int(input("Zadejte číslo, kterým má být předchozí číslo vyděleno: "))
        if y==0:
            print("Nelze dělit nulou.")
        else:
            Vydelit(y)
        continue
    else:
        break
#2
evidence=[]
print("1 – Přidat do evidence")
print("2 – Smazat z evidence")
print("3 – Hledat v evidenci")
print("4 – Vypsat evidenci")
print("Cokoliv jiného – KONEC")
while True:
    akce=int(input("Zadejte číslo operace: "))
    if akce==1:
        y=input("Zadejte jméno, které chcete přídat do evidence: ")
        Pridej(y)
        continue
    elif akce==2:
        y=input("Zadejte jméno, které chcete smazat z evidence: ")
        if y in evidence:
            Smaz(y)
        else:
            print("Zadané jméno není v evidenci.")
        continue
    elif akce==3:
        y=input("Zadejte jméno, které chcete vyhledat v evidenci: ")
        Zjisti(y)
        continue
    elif akce==4:
        Vypis()
        continue
    else:
        break