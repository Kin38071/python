# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 08:11:52 2022

@author: kin38071
"""

from tkinter import *
from tkinter import messagebox as msb

hlavni=Tk()
hlavni.minsize(300,80)


hornimenu=Menu(hlavni)

menuText=Menu(hornimenu,tearoff=0)
menuText.add_command(label="Jaro",command=lambda:vystup.config(text="Jaro"))
menuText.add_command(label="Léto",command=lambda:vystup.config(text="Léto"))
menuText.add_command(label="Podzim",command=lambda:vystup.config(text="Podzim"))
menuText.add_command(label="Zima",command=lambda:vystup.config(text="Zima"))
hornimenu.add_cascade(label="Text",menu=menuText)

menuBarva=Menu(hornimenu,tearoff=0)
menuBarva.add_command(label="Červená",command=lambda:vystup.config(bg="red"))
menuBarva.add_command(label="Modrá",command=lambda:vystup.config(bg="blue"))
menuBarva.add_command(label="Zelená",command=lambda:vystup.config(bg="green"))
menuBarva.add_separator()
menuBarva.add_command(label="Bílá",command=lambda:vystup.config(bg="white"))
menuBarva.add_command(label="Fialová",command=lambda:vystup.config(bg="purple"))
hornimenu.add_cascade(label="Barva",menu=menuBarva)

menuNapoveda=Menu(hornimenu,tearoff=0)
menuNapoveda.add_command(label="O programu",command=lambda:msb.showinfo("O programu","Zkušební program na menu\nVytvořil autor"))
hornimenu.add_cascade(label="Nápověda",menu=menuNapoveda)

hornimenu.add_command(label="Konec", command=hlavni.destroy)


hlavni.config(menu=hornimenu)


vystup=Label(hlavni,text="Období",font="Arial 20 bold",bg="white",width=15, height=5)
vystup.pack(padx=10,pady=10)


hlavni.mainloop()