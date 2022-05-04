"""
#Spinbox - pro výběr čísel

from tkinter import *

def Nastav():
    #vystup["text"]=cisla.get()     #použiji buď název komponenty
    vystup["text"]=v.get()          #nebo připojenou proměnnou

hlavni=Tk()

v=StringVar()
v.set("0")

#cisla=Spinbox(hlavni,from_=-50,to=1000,increment=5,textvariable=v,command=Nastav)
cisla=Spinbox(hlavni,values=(0,1,2,4,7,11,25),textvariable=v)    #specifikace hodnot
cisla.pack(padx=5,pady=5)

vystup=Label(hlavni,text="0",font="Arial 20",textvariable=v)
vystup.pack(padx=5,pady=5)

hlavni.mainloop()

#OptionMenu - rozbalovací menu pro výběr jedné možnosti z nabídky

from tkinter import *

def Nastav(hodnota):
    print("Nastavená je",v.get(),hodnota)

hlavni=Tk()

v=StringVar()
v.set("jedna")

vyber=OptionMenu(hlavni,v,"jedna","dva","tři",command=Nastav)
vyber.configure(width=15)
vyber.pack(padx=5,pady=5)

hlavni.mainloop()

#seznam parametrů
from tkinter import *

hlavni=Tk()

parametry=["první","druhá","třetí"]

v=StringVar()
v.set(parametry[0])

vyber=OptionMenu(hlavni,v,*parametry)
vyber.pack(padx=5,pady=5)

hlavni.mainloop()

#Hodnoty v OptionMenu ze souboru

from tkinter import *

mena=[]
soubor=open("listek.txt","r")
while True:
    kod=soubor.read(3)
    mena.append(kod)
    soubor.readline()
    if kod=="":
        break
soubor.close()
mena.pop()
print(mena)


hlavni=Tk()

v=StringVar()
v.set(mena[0])

vyber=OptionMenu(hlavni,v,*mena)
vyber.pack(padx=5,pady=5)

hlavni.mainloop()
"""
#Standardní dialogy

from tkinter import *
from tkinter import messagebox as msb

def Zprava():
    msb.showinfo("Informace","Přečtěte si, prosím, \nnásledující informace")
    #showwarning,showerror

def Dotaz():
    x=msb.askyesno("Otázka","Opravdu chcete skončit?")
    #askokcancel,askretrycancel,askquestion (vrací hodnoty "yes" a "no")
    print(x)
    if x:
        hlavni.destroy()
    else:
        msb.showinfo("Návrat","Tak ne")

hlavni=Tk()

zprava=Button(hlavni,text="Zpráva",width=10,command=Zprava)
zprava.pack(padx=5,pady=5)

dotaz=Button(hlavni,text="Dotaz",width=10,command=Dotaz)
dotaz.pack(padx=5,pady=5)


hlavni.mainloop()















