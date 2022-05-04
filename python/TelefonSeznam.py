# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:49:26 2021

@author: kin38071
"""
cisla = {}
while True:
    print("1: Přidání dalšího záznamu")
    print("2: Seřazený výpis všech jmen v seznamu")
    print("3: Vyhledání čísla podle zadaného jména")
    print("4: Výpis všech jmen a telefonních čísel pod sebe")
    print("jiná volba, než uvedená v menu, znamená konec aplikace.")
    volba=int(input("Zadejte volbu: "))
    if volba == 1:
        klic=input("Zadejte jméno: ")
        hodnota=input("Zadejte čílo: ")
        cisla[klic]=hodnota
        print()
        continue
    elif volba == 2:
        seznam=list(cisla)
        seznam.sort()
        for i in seznam:
            print(i)
        continue
    elif volba == 3:
        x=input("Zadejte jméno: ")
        if x in cisla:
            print(cisla[x])
        else:
            print("Zadané jméno není v seznamu")
        print()
        continue
    elif volba == 4:
        for i in cisla:
            print(i,cisla[i])
        print()
        continue
    else:
        break