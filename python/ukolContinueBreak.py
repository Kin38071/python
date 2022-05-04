# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:58:53 2021

@author: Jan
"""
import random
#1
pocet=int(input("Zadejte, kolikrát chcete hodit kostkou: "))
hod=0
celkem=0
while hod<pocet:
    hod=hod+1
    kostka=random.randint(1,6)
    celkem=celkem+kostka
    print(str(hod)+": kostka hodila",kostka)
prumer=celkem/pocet
print("Průměrná hodnota hodu je",prumer)
#2
print()
print("Zkus uhodnout číslo, které si myslím")
cislo=random.randint(0,100)
pocet=1
while True:
    hadani=int(input("Zadejte číslo: "))
    if hadani>cislo:
        print("Vedle, zkus hádat menší číslo!")
        pocet=pocet+1
        continue
    if hadani<cislo:
        print("Vedle, zkus hádat větší číslo!")
        pocet=pocet+1
        continue
    else:
        print("Trefa!")
        break
print("Gratuluji, potřeboval jsi",pocet,"pokusů k uhodnutí čísla.")