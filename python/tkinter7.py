# Canvas - kreslící plátno
"""
from tkinter import *
from turtle import width

from matplotlib.pyplot import fill

hlavni = Tk()

platno = Canvas(hlavni, width=200, height=100, bg="white")
platno.pack()

platno.create_line(0, 0, 200, 100, fill="blue", width=2)
platno.create_line(0, 100, 200, 0, fill="red", width=2)
platno.create_rectangle(50, 25, 150, 75, fill="lightgreen", outline="green")
platno.create_oval(75, 25, 125, 75, fill="yellow")
platno.create_polygon(100, 20, 80, 80, 120, 80, fill="magenta")


hlavni.mainloop()
"""
# Vytvoření tabulky - jednorozměrná
"""
from tkinter import *
import random
from matplotlib.pyplot import fill

hlavni = Tk()

sez = []

for i in range(20):
    txt = StringVar()
    txt.set("Tlačítko "+str(i+1))
    b = Button(hlavni, textvariable=txt)
    sez.append(b)
    sez[i]["bg"] = "#{:02x}{:02x}{:02x}".format(random.randint(
        0, 255), random.randint(0, 255), random.randint(0, 255))
    # if i % 2 == 0:
    #sez[i]["bg"] = "red"
    # else:
    #sez[i]["bg"] = "blue"
    b.pack(fill=X)

sez[13]["state"] = DISABLED


hlavni.mainloop()
"""
#Tabulka - dvourozměrná
from tkinter import *

hlavni = Tk()

sez=[]

for i in range(5):
    for j in range(10):
        txt = StringVar()
        txt.set(str(i+1)+","+str(j+1))
        b = Button(hlavni, width=5, textvariable=txt)
        sez.append(b)
        b.grid(row=j,column=i)


hlavni.mainloop()
