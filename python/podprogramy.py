# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:32:35 2021

@author: Jan
"""
#Podprogramy - Funkce
"""
def Nazev(parametr1,parramtetr2,...):
    blok příkazů
    return výsledný výraz

#funkce bez parametru

def Pozdrav():              #Definice funkce
    print("Dobré ráno")

Pozdrav()                   #Volání funkce

#funkce s 1 parametrem

def Pozdravy(pocet):
    for i in range(pocet):
        print("Ahoj")

kolik=int(input("Zadej počet opakování: "))        
Pozdravy(kolik)

#funkce s více parametry

def Superpozdrav(pocet,text):
    for i in range(pocet):
        print(text)
        
x=int(input("Zadej počet opakování: "))
y=input("Zadej pozdrav: ")

Superpozdrav(x,y)

#funkce s návratovou hodnotou
def Mocnina(x):
    y=x**2
    return y

cislo=int(input("Zadej číslo: "))
print("Mocnina =",Mocnina(cislo))

#Implicitní parametry
def Mocnina(x,y=2):
    return x**y

print(Mocnina(5))
print(Mocnina(5,3))

#Jména parametrů
def funkce(a,b,c="c",d=4,e=10):
    print(a,b,c,d,e)

funkce(b="B",a="a",e=20)
"""
#Proměnlivý počet parametrů
def funkce2(a,b,c=5,*ostatni):
    print(a,b,c)
    print(ostatni)
    
seznam=[8,9,3,6,7]

funkce2(3,4)
print("########")
funkce2(3,4,5,6,7,8)

funkce2(1,2,3,seznam)
funkce2(1,2,3,*seznam)