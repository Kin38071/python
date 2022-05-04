# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:43:51 2021

@author: Jan
"""
"""
veta="Kobyla má malý bok"
if "m" in veta:
    print("Věta obsahuje písmeno \"m\"")
p=0
for znak in veta:
    print(znak)
    if znak=="a":
        print("Našel jsem \"a\"")
        p+=1
print("Počet \"a\":",p)
"""
#Metody
#Náhrada textu - replace(vyhledávaný podřetězec,řetězec pro náhradu)
"""
ret="Jedna dvě, Honza jde, nese pytel s brouky"
ret2=ret.replace("s brouky","mouky")
print(ret2)

retezec="Haf, ňaf, blaf, řekl pejsek"
print(retezec.replace("af","afiky"))    #nahradí všechny výskyty
print(retezec.replace("af","afiky",1))  #nahradí první výskyt

#Vyhledávání textu - find()
ret="Toto je dlouhý řetězec, ve kterém je podřetězec"
print(ret.find("moc"))
print(ret.find("řetězec"))

#Změna velikosti písmen
text="TEXT pro záměnu MALÝCH a velkých pÍSmen"
print("Všechna malá: ",text.lower())
print("Všechna velká: ",text.upper())
print("První velké: ",text.capitalize())
print("Záměna malá/velká: ",text.swapcase())
"""
#Funkce pro manipulace s jednotlivými znaky:
#ord(c) - převádí znaky na celá čísla (vrací pořadové číslo znaku c)
#chr(i) - vrací znak s pořadovým číslem i

print("ASCII kód znaku A =",ord("A"))
print("Pod kódem 65 je",chr(65))