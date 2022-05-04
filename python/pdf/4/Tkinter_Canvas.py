#Canvas - plátno

from tkinter import *

hlavni=Tk()

#Vytvoření komponenty
platno=Canvas(hlavni,width=200,height=100,bg="black")
platno.pack()

#vykreslení úsečky (souřadnice začátku a konce, barva, šířka)
platno.create_line(0,0,200,100,fill="yellow",width=2)
platno.create_line(0,100,200,0,fill="red",width=2)
#vykreslení čtyřúhelníka (souřadnice levého horního a pravého spodního rohu, barva výplně, barva obrysu)
platno.create_rectangle(50,25,150,75,fill="lightblue",outline="blue")
#vykreslení elipsy/kružnice
platno.create_oval(75,25,125,75,fill="green",outline="lightgreen")
#vykreslení mnohoúhelníka (dle počtu souřadnic vrcholů)
platno.create_polygon(100,20,80,80,120,80,fill="magenta")

hlavni.mainloop()
