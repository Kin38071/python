# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 08:03:31 2021

@author: kin38071
"""
#1
znaky=[]
soubor=open("text.txt","r")
soub=open("opacne.txt","w")
radky=soubor.read()
for znak in radky:
    znaky.append(znak)
for i in znaky[::-1]:
    soub.write(i)
soub.close()
soubor.close()
#2
soubor=open("text.txt","r")
sou=open("zamena.txt","w")
c=0
while True:
    prv=input("vyberte znak, který chcete zaměnit: ")
    for i in prv:
        c=c+1
    if c>1 or c==0:
        print("Zadejte pouze JEDEN znak")
        c=0
        continue
    else:
        c=0
        break

while True:
    drh=input("vyberte znak, kterým chcete zaměnit předchozí znak: ")
    for i in drh:
        c=c+1
    if c>1 or c==0:
        print("Zadejte pouze JEDEN znak")
        c=0
        continue
    else:
        c=0
        break

radky=soubor.read()
for znak in radky:
    if znak==prv:
        sou.write(drh)
    else:
        sou.write(znak)
sou.close()
soubor.close()

#3
c=0
soubor=open("PYRAMIDA.txt","w")
while True:
    p=input("Zadejte jedno písmeno: ")
    for i in p:
        c=c+1
    if c>1 or c==0:
        print("Zadejte pouze JEDNO písmeno")
        c=0
        continue
    else:
        c=0
        break

for i in range(100):
    for j in range(i+1):
        soubor.write(p)
    soubor.write("\n")

soubor.close()
#4
soubor=open("CISLA.txt","w")
n=int(input("Zadejte číslo: "))
c=n
suma=0
pom=0
for i in range(n+2):
    suma=suma+c
    if c==0:
        for i in str(suma):
            pom=pom+1
            for i in str(pom):          
                soubor.write("-")
        soubor.write("\n{:}".format(suma))
        break
    else:
        soubor.write("{:}\n".format(c))
        c=c-1

soubor.close()
