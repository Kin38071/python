#Graf podle zadání uživatele

from tkinter import *
from tkinter import colorchooser as clr
import pylab as py

#Ukládání souřadnic do seznamů
def Uloz():
    global x_ove
    global y_ove
    x_ove.append(float(bodx.get()))
    y_ove.append(float(body.get()))
    vstupx.delete(0,END)
    vstupx.focus_set()
    vstupy.delete(0,END)
    vypis.delete(1.0,END)
    vypis.insert(1.0,x_ove)
    vypis.insert(END,"\n")
    vypis.insert(END,y_ove)

#Vykreslení grafu
def Graf():
    x=py.array(x_ove)
    y=py.array(y_ove)
    py.plot(x,y,color=brv,linewidth=int(T.get()))
    py.title(nazev.get())
    py.xlabel(nazevOX.get())
    py.ylabel(nazevOY.get())
    if M.get()==1:
        py.grid(True)
    py.show()

#Výběr barvy
def Barva():
    global brv
    b=clr.askcolor(title="Vyber barvu pro čáru")
    brv=b[1]
    barva["fg"]=brv

hlavni=Tk()
hlavni.title("Grafy II")


#proměnné pro souřadnice
bodx=StringVar()
body=StringVar()
x_ove=[]
y_ove=[]

#proměnné pro vlastnosti grafu
nazev=StringVar()
nazevOX=StringVar()
nazevOY=StringVar()
M=IntVar()          #mřížka
T=StringVar()       #tloušťka čáry
brv="black"


#Vzhled aplikace - zadávání souřadnic
ram=LabelFrame(hlavni,text="Zadání souřadnic",bd=2,relief="ridge",padx=5,pady=5)
ram.pack(padx=10,pady=10)

popis1=Label(ram,text="Souřadnice x",font="Calibri 10")
popis1.grid(pady=3)
vstupx=Entry(ram,font="Calibri 10",textvariable=bodx)
vstupx.grid(row=0,column=1,pady=3)

popis2=Label(ram,text="Souřadnice y",font="Calibri 10")
popis2.grid(row=1,pady=3)
vstupy=Entry(ram,font="Calibri 10",textvariable=body)
vstupy.grid(row=1,column=1,pady=3)

uloz=Button(ram,text="Ulož a další",width=15,font="Calibri 12",command=Uloz)
uloz.grid(row=2,columnspan=2,pady=2)

#Vzhled aplikace - vlastnosti grafu
ram2=LabelFrame(hlavni,text="Vlastnosti grafu",bd=2,relief="ridge",padx=5,pady=5)
ram2.pack(padx=5,pady=5)

popis3=Label(ram2,text="Název grafu",font="Calibri 10")
popis3.grid(padx=3)
vstupN=Entry(ram2,font="Calibri 10",textvariable=nazev)
vstupN.grid(row=0,column=1,pady=3)

popis4=Label(ram2,text="Název osy X",font="Calibri 10")
popis4.grid(row=1,padx=3)
vstupOX=Entry(ram2,font="Calibri 10",textvariable=nazevOX)
vstupOX.grid(row=1,column=1,pady=3)

popis5=Label(ram2,text="Název osy Y",font="Calibri 10")
popis5.grid(row=2,padx=3)
vstupOY=Entry(ram2,font="Calibri 10",textvariable=nazevOY)
vstupOY.grid(row=2,column=1,pady=3)

mrizka=Checkbutton(ram2,text="Mřížka",font="Calibri 10",variable=M)
mrizka.grid(row=3,column=0,pady=3)

popis6=Label(ram2,text="Tloušťka čáry",font="Calibri 10")
popis6.grid(row=4,padx=3)
tloustka=Spinbox(ram2,from_=1,to=10,textvariable=T)
tloustka.grid(row=4,column=1,pady=3)

barva=Button(ram2,text="Barva čáry",font="Calibri 12",width=15,command=Barva)
barva.grid(row=5,columnspan=2,pady=3)


kresligraf=Button(hlavni,text="Vykresli graf",width=15,font="Calibri 12 bold",command=Graf)
kresligraf.pack(pady=10)

#Pro zobrazení zadávaných souřadnic
vypis=Text(hlavni,height=4,width=50)
vypis.pack()




hlavni.mainloop()











