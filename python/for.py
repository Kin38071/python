# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:42:08 2020

@author: Jan
"""

#cykly - řízené opakování sekvence příkazů
#cyklus for - řízený parametrem (když vím, kolikrát má proběhnout)
"""
#1. způsob použití
for proměnná in sekvence:
    příkazy

for i in ("a","b","c"):
    print(i)

text="Pátek"
for i in text:
    print(i)

#2. způsob použití
for i in range(mez):
    příkazy
#i nabývá hodnot od 0 do mez-1, při každém průchodu cyklem se zvětšuje o 1

for i in range(10):
    print(i)

for i in range(dolnímez,hornímez):
    příkazy
#i nabývá hodnot od dolní meze do mez-1, při každém průchodu cyklem se zvětšuje o 1

for i in range(2,12):
    print(i)

for i in range(dolnímez,hornímez,krok):
    příkazy
#i nabývá hodnot od dolní meze do mez-1, při každém průchodu cyklem se zvětšuje o krok

for i in range(1,20,2):
    print(i)

for i in range(1,11):
    print(i)

for i in range(10,0,-1):
    print(i)
"""
x=0
for i in range(1,11):
    x=x+i       #s+=i
print(x)
