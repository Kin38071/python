# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 08:28:27 2021

@author: kin38071
"""
sez=[]
pis={}
ost={}
soubor=open("text.txt","r")
radky=soubor.read()
for znak in radky:
    if znak!="\n":
        sez.append(znak.lower())
soubor.close()
pismena=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ostatni=[".",",",":","?","!","0","1","2","3","4","5","6","7","8","9"]
for i in pismena:
    if i in sez:
        pis[i]=sez.count(i)
pp=0
for i in pis:
    print("{}: {}".format(i,pis[i]))
    pp+=pis[i]
print("Počet písmen:",pp)

for i in ostatni:
    if i in sez:
        ost[i]=sez.count(i)
po=0
for i in ost:
    po+=ost[i]
print("Počet ostatních znaků:",po)