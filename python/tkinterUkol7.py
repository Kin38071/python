from tkinter import *
import random

#1

hlavni = Tk()

platno = Canvas(hlavni, width=500, height=500, bg="black")
platno.pack()

platno.create_line(random.randint(0,500), random.randint(0,500), random.randint(0,500), random.randint(0,500), fill="blue", width=2)
platno.create_line(random.randint(0,500), random.randint(0,500), random.randint(0,500), random.randint(0,500), fill="red", width=2)
platno.create_line(random.randint(0,500), random.randint(0,500), random.randint(0,500), random.randint(0,500), fill="green", width=2)
platno.create_line(random.randint(0,500), random.randint(0,500), random.randint(0,500), random.randint(0,500), fill="yellow", width=2)
platno.create_line(random.randint(0,500), random.randint(0,500), random.randint(0,500), random.randint(0,500), fill="magenta", width=2)

hlavni.mainloop()

#2

hlavni = Tk()

for i in range(5):
    for j in range(10):
        txt = StringVar()
        txt.set(str(i+1)+","+str(j+1))
        b = Entry(hlavni, width=4, textvariable=txt)
        b.configure(bg="#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        b.grid(row=j,column=i)

hlavni.mainloop()