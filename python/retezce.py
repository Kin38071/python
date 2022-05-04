# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Řetězce
#print("""Toto
#je
#delší
#text""")

#speciální (escape) znaky
#apostrofa, uvozovka, lomítko, nový řádek, tabulátor
"""
print("Dny v týdnu: \nPondělí \nÚterý \n\na tak dále...\tNeděle")
print("Speciální \"znaky\":\'\\")
"""
"""#Indexování a operátor slice (:)
x="pokusny text"
print("znak s indexem 3:",x[3])
print("třetí od konce:",x[-3])

print("první 2 znaky:",x[:2])
print("od znaku s indexem 2:",x[2:])
print("poslední 3 znaky:",x[-3:])
print("od znaku s indexem 1 po 4:",x[1:4])

print("každý 2 znak:",x[::2])
print("od znaku s indexem 2 každý třetí:",x[2::3])
"""
"""#Základní operace
#sčítání, násobení celým číslem, zjištění délky

pozdrav="Ahoj"
pozdrav2=pozdrav+" Karle"
print(pozdrav2)
print(pozdrav*10)
print(len(pozdrav2)) #délka řetězce
"""
"""#Formátování řetězce
#retezec="{index:specifikace}".format(n-tice)

ret="Dnes je {0}.{1}.{2}".format(22,1,2021)
print(ret)

print("Od {} do {}".format("rána","22:00"))

print("{0} i {1}".format("ano","ne"))
print("{1} i {0}".format("ano","ne"))
print("{1} a {1} a {1}".format("ano","ne"))

print("Jmenuji se {name}".format(name="Pavel"))
"""
#lze specifikovat šířku, zarovnání, počet des. míst a způsob prezentace dat
#např. b = binární formát, d = dekadické celé číslo, f = reálné číslo, x = hexadecimální formát
#x = hexadec. formát
import math
import random
print("{:<25}".format("zarovnáno vlevo"))
print("{:>25}".format("zarovnáno vpravo"))
print("Číslo {0:^15} zarovnané na střed".format(28))
print("Číslo {0:*^15} zarovnané na střed".format(28))

print("Hodnota Pí je asi {0:.3f}".format(math.pi))

print("{0:<10.1f} => {0:10.0f}".format(3/4))

print("Dnes je {0:b}.{1:b}.{2:b}".format(22,1,2021))
print("Dnes je {0:x}.{1:x}.{2:x}".format(22,1,2021))

print("Náhodná barva: {:02x}{:02x}{:02x}".format(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

for i in range(7,11):
    print("{0:2}{1:4}{2:5}".format(i,i**2,i**3))
