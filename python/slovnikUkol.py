# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 08:11:20 2021

@author: kin38071
"""
import random

DB={}
DB['Mirek']=['Mirek','Palackeho 16','Olomouc','732 675 810']
DB['Dana']=['Dana','Litovelska 7','Olomouc','775 321 405']
DB['Jana']=['Jana','Husova 7','Litovel','775 321 405']
DB['Pepa']=['Pepa','Komenskeho 9','Praha','845 207 536']
DB['Marek']=['Marek','Jarni','Olomouc','776 345 890']
DB['Michal']=['Michal','Mezice 20','Mezice','606 267 762']
DB['Petra']=['Petra','Neznama 34','Olomouc','731 456 789']
jmeno=0
ulice=1
mesto=2
telefon=3

#a
jme=input("Zadejte jméno: ")
uli=input("Zadejte ulici: ")
mes=input("Zadejte město: ")
cis=input("Zadejte číslo: ")
DB[jme]=[jme,uli,mes,cis]
print(DB)
print("")
#b
for kl in DB:
    if DB[kl][mesto]=="Olomouc":
        print(DB[kl])
print("")
#c
for kl in DB:
    if DB[kl][mesto]=="Olomouc":
        DB[kl][mesto]="Opava"
        print(DB[kl])
print("")
#d
for kl in DB:
    DB[kl].append(random.randint(15,25))
    print(DB[kl])
print("")
#e
for kl in DB:
    if DB[kl][telefon][0]=="7":
        print(DB[kl])