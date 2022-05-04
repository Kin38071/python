# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 08:58:56 2021

@author: kin38071
"""
import random
#1
soubor=open("pokus.txt","r")
file=open("kopie.txt","w")
for radek in soubor:
    file.write(radek)
soubor.close()
file.close()
#2
soubor=open("vstup.txt","w")
file=open("vystup.txt","w")
for i in range(100):
    x=random.randint(10,99)
    y=random.randint(10,99)
    soubor.write("{:>2} {:>2}\n".format(x,y))
soubor.close()
soubor=open("vstup.txt","r")
radek=soubor.readlines()
for i in radek:
    c1=int(i[0])+int(i[1])
    c2=int(i[3])+int(i[4])
    file.write("{:>2} + {:>2} = {:>3}\n".format(c1,c2,c1+c2))
soubor.close()
file.close()
#3
a=0
soubor=open("pismena.txt","r")
radky=soubor.read()
for znak in radky:
    if znak == "a":
        a=a+1
print("a =",a)
soubor.close()
#4
soubor=open("cisla.txt","w")
for i in range(10):
    c=random.randint(1,100)
    soubor.write("{:>3} {:>5}\n".format(c,c**2))
soubor.close()