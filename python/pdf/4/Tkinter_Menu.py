#Menu

from tkinter import *
from tkinter import messagebox as msb

#Souhrnná funkce pro položky menu Soubor
def Hlaska(a):
    msb.showinfo(a,"Není naprogramováno")

#Funkce pro položku checkbutton
def Pokus():
    if v1.get()==1:
        vystup1["text"]="Zapnuto"
    else:
        vystup1["text"]="Vypnuto"

#Funkce pro položky radiobutton
def Prep():
    vystup2["text"]=volby[v2.get()]

hlavni=Tk()
hlavni.minsize(300,80)

hornimenu=Menu(hlavni)    #vytvoření hlavního menu

#hornimenu.add_command(label="Soubor",command=lambda:Hlaska("Soubor"))
#vytvoření rozbalovacího menu
menuSoubor=Menu(hornimenu,tearoff=0)
menuSoubor.add_command(label="Otevřít")
menuSoubor.add_command(label="Uložit")
menuSoubor.add_separator()     #oddělovací čára
menuSoubor.add_command(label="Konec",command=hlavni.destroy)
hornimenu.add_cascade(label="Soubor",menu=menuSoubor) #připojení k hlavnímu menu

#druhé rozbalovací menu
v1=IntVar()   #proměnná pro checkbutton
v2=IntVar()   #proměnná pro radiobutton
v2.set(0)
volby=["první","druhý","třetí"] 

menuUpravy=Menu(hornimenu,tearoff=0)
menuUpravy.add_command(label="Vyjmout")
menuUpravy.add_command(label="Kopírovat")
menuUpravy.add_command(label="Vložit")
menuUpravy.add_separator()
menuUpravy.add_checkbutton(label="Pokus",variable=v1,command=Pokus)
menuUpravy.add_separator()
menuUpravy.add_radiobutton(label="1",variable=v2,value=0,command=Prep)
menuUpravy.add_radiobutton(label="2",variable=v2,value=1,command=Prep)
menuUpravy.add_radiobutton(label="3",variable=v2,value=2,command=Prep)
hornimenu.add_cascade(label="Úpravy",menu=menuUpravy)

hornimenu.add_command(label="Nastavení",command=lambda:Hlaska("Nastavení"))
hornimenu.add_command(label="Nápověda",command=lambda:Hlaska("Nápověda"))
hornimenu.add_command(label="Konec",command=hlavni.destroy)

hlavni.config(menu=hornimenu)  #připojení hlavního menu do hlavního formuláře


vystup1=Label(hlavni,text="Vypnuto",font="Arial 12 bold")
vystup1.pack(padx=5,pady=5)
vystup2=Label(hlavni,text=volby[0],font="Arial 12 bold")
vystup2.pack(padx=5,pady=5)

hlavni.mainloop()









    
