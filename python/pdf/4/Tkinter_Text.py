#Text - pro delší texty

from tkinter import *

#mazání textu
def Smazat():
    text.delete(1.0,END)     #smaže vše
    text.focus_set()         #nastavení kurzoru
    #text.delete(1.0,2.0)    #smaže první řádek
    #text.delete(2.0,END)    #od druhého řádku do konce
    #text.delete(INSERT,END) #od místa kurzoru do konce
    #text.delete(INSERT)     #jeden znak

#přečtení textu
def Precist():
    ret=text.get(1.0,END)     #přečte celý obsah komponenty
    #ret=text.get(1.0,2.0)    #přečte první řádek
    #ret=text.get(2.0,END)    #od druhého řádku do konce
    #ret=text.get(INSERT,END) #od místa kurzoru do konce
    #ret=text.get(INSERT)     #znak vpravo od kurzoru
    print(ret)

hlavni=Tk()

text=Text(hlavni,font="Arial 10")
text.pack()

#vložení textu
text.insert(END,"ahoj")   #vkládáme text na konec
text.insert(1.0,"Karle")  #vkládáme text na začátek prvního řádku
#INSERT - místo kurzoru

#vložení textu se stylem
text.tag_config("modre",font="20",foreground="blue",underline=1)
text.insert(END,"\n")
text.insert(END,"ahoj","modre")
text.insert(END," světe")

text.insert(END,"\n")
text.insert(END,"ahoj, světe","cervene")
text.tag_config("cervene",foreground="red",font="Arial 20 bold")

smazat=Button(hlavni,text="Smazat",width=10,command=Smazat)
smazat.pack(padx=5,pady=5,side=LEFT)
precist=Button(hlavni,text="Přečíst",width=10,command=Precist)
precist.pack(padx=5,pady=5,side=LEFT)

hlavni.mainloop()











