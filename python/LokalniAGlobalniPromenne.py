# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:54:12 2021

@author: Jan
"""

#Funkce - lokální a globální proměnné
"""
def funkce1():
	x=10		#vznik lokální proměnné
	print(x)	#tisk lokální proměnné

funkce1()
print(x)		#pokus o tisk proměnné, která neexistuje

def funkce2(x):     #použití globální proměnné jako parametru
	#x=10		#vznik lokální proměnné
	x=x*2
	print(x)	#tisk lokální proměnné

x=1			#vznik globální proměnné
funkce2()
print(x)		#tisk globální proměnné

def funkce2():
    global x #definice globální proměnné
    x=x*2
    print(x)
    
x=1
funkce2()
print(x)

#Použití globální proměnné jako parametru mezi funkcemi
def vyp1(x):
    x=x*2
    print(x)
    
def vyp2(x):
    x=x+1
    print(x)
    
x=10
vyp1(x)
vyp2(x)
"""
#Použití globální proměnné s předáním hodnoty
def vyp1():
    global x
    x=x*2
    print(x)
    
def vyp2():
    global x
    x=x+1
    print(x)

x=10
vyp1()
vyp2()