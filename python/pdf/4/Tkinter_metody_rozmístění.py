"""
#metoda pack - doplnění
from tkinter import *

def Mocnina():
    x=int(vstup.get())   #x=float(vstup.get())
    vystup["text"]=str(x**2)
    vstup.select_range(0,END)

hlavni=Tk()
hlavni.minsize(300,200)

ram=Frame(hlavni,width=100,height=50,relief="ridge",bd=2,padx=10,pady=10)
ram.pack(padx=5,pady=5)

vstup=Entry(ram)
vstup.focus_set()
vstup.pack(side="left",padx=5,pady=5)

vystup=Label(ram,text="Výsledek",width=10)
vystup.pack(side="left",padx=5,pady=5)

vypocet=Button(hlavni,text="Mocnina",width=15,command=Mocnina)
#vypocet.pack(anchor=W,padx=10,pady=10)          #anchor = zarovnání (W/E)
#vypocet.pack(fill=X,padx=10,pady=10)            #fill = roztažení vodorovné
#vypocet.pack(fill=Y,expand=1,padx=10,pady=10)   #roztažení svislé
vypocet.pack(fill=BOTH,expand=1,padx=10,pady=10) #roztažení v obou směrech

hlavni.mainloop()

#metoda place
from tkinter import *

hlavni=Tk()

vstup=Entry(hlavni,width=20)
vstup.place(x=65,y=25) #souřadnice levého horního rohu komponenty
#počátek je v levém horním rohu okna

napis=Label(hlavni,text="Text")
napis.place(x=25,y=25)

akce=Button(hlavni,text="Akce",width=15)
akce.place(x=65,y=85)

hlavni.mainloop()
"""
#metoda grid

from tkinter import *

hlavni=Tk()

jmeno=Label(hlavni,text="Jméno:")
jmeno.grid(row=0,column=0,sticky=E)
#řádek 0, sloupec 0 (nulový sloupec psát nemusíme)
#sticky = zarovnání/roztažení (zde zarovnání doprava)

prijmeni=Label(hlavni,text="Příjmení:")
prijmeni.grid(row=1,column=0,sticky=E)
#řádek 1, sloupec 0, zarovnání doprava

vstup1=Entry(hlavni)
vstup1.grid(row=0,column=1,padx=5,pady=5)

vstup2=Entry(hlavni)
vstup2.grid(row=1,column=1,padx=5,pady=5)

kontrola=Label(hlavni,text="Kontrola",bg="magenta")
kontrola.grid(row=2,columnspan=2,sticky=W+E,padx=5,pady=5)
#řádek 2, sloupec 0 (nemusíme psát), přesah přes 2 sloupce, roztažení vodorovné

akce=Button(hlavni,text="Akce",width=10)
akce.grid(row=3,sticky=W,padx=5,pady=5)

konec=Button(hlavni,text="Konec",width=10)
konec.grid(row=3,column=1,sticky=E,padx=5,pady=5)

pokus=Label(hlavni,text="Pokus",bg="lightblue")
pokus.grid(row=0,column=2,rowspan=4,sticky=N+S,padx=5,pady=5)
#řádek 0, sloupec 2, přesah přes 4 řádky, roztažení svislé


hlavni.mainloop()








































































