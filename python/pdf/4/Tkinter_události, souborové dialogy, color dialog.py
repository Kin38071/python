#Události
#komponenta.bind(udalost,ovladac)
"""
from tkinter import *

def LevyKlik(udalost):
    print("Kliknuto na pozici:",udalost.x,udalost.y)

def Najeti(udalost):
    print("Najel jsi na rám")

def Pryc(udalost):
    print("Jsi mimo")

def Klavesa(udalost):
    print("Stiskl jsi",udalost.char)

hlavni=Tk()

ram=Frame(hlavni,width=100,height=100,bd=2,bg="black")
ram.bind("<Button-1>",LevyKlik)  #stisk levého tlačítka myši
#"<Button-2>" = prostřední tlačítko myši
#"<Button-3>" = pravé tlačítko myši
#"<Double-Button-1>" = dvojklik levým tlačítkem, atd.
ram.bind("<Enter>",Najeti)   #najetí myší na komponentu
ram.bind("<Leave>",Pryc)     #odjetí myši z komponenty
ram.pack()
vstup=Entry(hlavni)
vstup.bind("<Key>",Klavesa)  #stisk "běžné" klávesy
vstup.pack(padx=5,pady=5)

hlavni.mainloop()
"""
#Souborové dialogy a barevný dialog
from tkinter import *
from tkinter import filedialog as fld   #modul pro souborové dialogy
from tkinter import colorchooser as clr #modul pro barevný dialog

def Otevrit():
    try:
        ret=fld.askopenfilename(title="Otevřít soubor")
        #print(ret)   #vrací cestu k souboru a jeho jméno
        soubor=open(ret,"r")
        cely=soubor.read()
        print(cely)
        soubor.close()
    except:pass

def Ulozit():
    try:
        ret=fld.asksaveasfilename(title="Uložit soubor",defaultextension="txt")
        soubor=open(ret,"w")
        soubor.write("aaaaaaaaaaa")
        soubor.close()
    except:pass

def Barva():
    barva=clr.askcolor(title="Výběr barvy")
    print(barva)   #dvouprvkový seznam [RGB tvar, Tk tvar]
    hlavni["bg"]=barva[1]

hlavni=Tk()

otevrit=Button(hlavni,text="Otevřít",width=10,command=Otevrit)
otevrit.pack(padx=5,pady=5)
ulozit=Button(hlavni,text="Uložit",width=10,command=Ulozit)
ulozit.pack(padx=5,pady=5)
vyberbarvy=Button(hlavni,text="Barva",width=10,command=Barva)
vyberbarvy.pack(padx=5,pady=5)


hlavni.mainloop()









