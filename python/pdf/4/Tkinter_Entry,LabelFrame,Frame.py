#Entry - vstupní řádek 
"""
from tkinter import *

def Smazat():
    vstup.delete(0,END)	       #smaže celý obsah
    #vstup.delete(0)           #smaže jeden znak
    #vstup.delete(0,INSERT)    #smaže text od začátku do pozice kurzoru
    #vstup.delete(INSERT,END)  #smaže text od pozice kurzoru do konce

def Vlozit():
    vstup.insert(0,"Něco jiného")	#vloží znak na zadanou pozici 
    #vstup.insert(END,"text")           #vloží text na konec
    #vstup.insert(INSERT,"text")        #vloží text na místo kurzoru

def Oznacit():
    vstup.select_range(0,END)		# označení celého textu

def Zobrazit():
    vystup["text"]=vstup.get()		#vrací současný obsah vstupního řádku(řetězec)


hlavni=Tk()

vstup=Entry(hlavni,width=20,bd=5)  #bd = okraj v pixelech
vstup.focus_set()                  #kurzor je nastaven v Entry
vstup.pack(padx=5,pady=5)

vystup=Label(hlavni,text="Výstup",font="Arial 15")
vystup.pack(pady=5)
    
smaz=Button(hlavni,text="Smaž",width=10,command=Smazat)
smaz.pack(pady=5)
vloz=Button(hlavni,text="Vlož",width=10,command=Vlozit)
vloz.pack(pady=5)
oznac=Button(hlavni,text="Označ",width=10,command=Oznacit)
oznac.pack(pady=5)
vypis=Button(hlavni,text="Vypiš",width=10,command=Vypsat)
vypis.pack(pady=5)

hlavni.mainloop()


#LabelFrame - rámeček s popisem
#použijeme předchozí program, ale upravíme ho tak, že všechna tlačítka budou v rámečku

from tkinter import *

def Smazat():
    vstup.delete(0,END)	

def Vlozit():
    vstup.insert(0,"Něco jiného")	

def Oznacit():
    vstup.select_range(0,END)		

def Vypsat():
    vystup["text"]=vstup.get()		


hlavni=Tk()

vstup=Entry(hlavni,width=20,bd=5)  
vstup.focus_set()                  
vstup.pack(padx=5,pady=5)

vystup=Label(hlavni,text="Výstup",font="Arial 15")
vystup.pack(pady=5)
    
skupina=LabelFrame(hlavni,text="Výběr akce",relief="groove",bd=2,padx=15,pady=15)
#padx, pady - zde vnitřní "vycpávky"
skupina.pack(padx=10,pady=10)

#všechny komponenty, které mají být uvnitř rámu, mají rodičovskou komponentu "skupina"
smaz=Button(skupina,text="Smaž",width=10,command=Smazat)
smaz.pack(pady=5)
vloz=Button(skupina,text="Vlož",width=10,command=Vlozit)
vloz.pack(pady=5)
oznac=Button(skupina,text="Označ",width=10,command=Oznacit)
oznac.pack(pady=5)
vypis=Button(skupina,text="Vypiš",width=10,command=Vypsat)
vypis.pack(pady=5)

hlavni.mainloop()
"""

#Frame - rámeček a umístění komponent vedle sebe
from tkinter import *

def Vypocet():
    x=int(vstup.get())					# x=float(vstup.get())
    vystup["text"]=str(x**2)
    vstup.select_range(0,END)

hlavni=Tk()
hlavni.title("Počítání")

ram=Frame(hlavni,bd=2,width=100,height=50,relief="ridge",padx=10,pady=10) 
ram.pack(padx=5,pady=5)

vstup=Entry(ram)
vstup.focus_set()
vstup.pack(side="left",padx=5,pady=5)  #side="left" - komponenta bude umístěna zleva

vystup=Label(ram,text="výsledek",width=10)
vystup.pack(side="left",padx=5,pady=5)

vyp=Button(hlavni,text="Druhá mocnina",width=15,command=Vypocet)
vyp.pack(padx=5,pady=5)

hlavni.mainloop()
