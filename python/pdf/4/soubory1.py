#Soubory

#první zápis do souboru
"""
nazev="mujprvnisoubor.txt"
soubor=open(nazev,"w")         #otevření souboru
vstup=input("Zadej text: ")
soubor.write(vstup)            #zápis do souboru

soubor.close()                 #uzavření souboru
#---------------------------------------------------------------------

soubor=open("mujprvnisoubor.txt","r+")
vstup=input("Zadej text: ")
soubor.write(vstup)

pozice=soubor.tell()   #aktuální pozice v souboru
print(pozice)

soubor.seek(5,0)       #přesun na danou pozici v souboru (5 znaků od začátku)     
soubor.write("******")

soubor.close()
#-----------------------------------------------------------------------

#Čtení ze souboru
soubor=open("text.txt","r")
text=soubor.readlines()        #přečte jako seznam řádků
print(text)

soubor.seek(0,0)               #přesun na začátek souboru
radek1=soubor.readline()       #přečte jeden řádek jako řetězec 
print(radek1)
radek2=soubor.readline()       #přečte další řádek
print(radek2)

cast1=soubor.read(5)           #přečte 5 znaků od dané pozice v souboru
print(cast1)
cast2=soubor.read(2)           #další dva znaky
print(cast2)
cast3=soubor.readline()        #zbytek řádku
print(cast3)
zbytek=soubor.read()           #celý zbytek souboru
print(zbytek)

soubor.close()

#Zápis textu a čísla

soubor=open("pokus.txt","w")
soubor.write("Dnes je krásně.\n")
soubor.write("Zítra bude pršet.\n")
soubor.write(str(1000000))

soubor.close()

#Čtení souboru řádek po řádku
soubor=open("pokus.txt","r")
cisloR=0
for radek in soubor:
    cisloR+=1
    print("Řádek",cisloR,":",radek,end="")
soubor.close()

#Zápis seznamu čísel
soubor=open("pokus.txt","a")
seznam=[5,48,74,89,544]
soubor.write("\n")
for cislo in seznam:
    soubor.write(str(cislo)+",")
soubor.close()
"""
#Zápis čísel do sloupců
import random

soubor=open("cisla.txt","w")
for i in range(10):
    c=random.randint(1,10)
    #soubor.write("{:>2}{:>5}{:>5}\n".format(c,c+5,c+10))
    soubor.write("{:>2}+{:>2}={:>2}\n".format(c,c+5,2*c+5))p
soubor.close()




































