# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:53:35 2020

@author: kin38071
"""

#př1
stranaA=float(input("Zadej délku strany A: "))
stranaB=float(input("Zadej délku strany B: "))
print("Obvod =",2*stranaA+2*stranaB)
print("Obsah =",stranaA*stranaB)

#př2
delkalatky=float(input("Zadej délku látky: "))
delkakusu=float(input("Zadej délku kusu, na který se má látka nastříhat: "))
print("Z látky můžeme nastříhat",delkalatky//delkakusu,"kusů")
print("Z látky zbyde",delkalatky%delkakusu)

#př3
cislo=int(input("Zadej celé číslo: "))
print("Poslední číslice je: ",cislo)
print("Předposlední číslice je: ",cislo)