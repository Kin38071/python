#Datum a čas - modul datetime

from datetime import *

dnes=datetime.now()
print(str(dnes))

print("Rok: {:d}".format(dnes.year))
print("Měsíc: {:02d}".format(dnes.month))
print("Den: {:02d}".format(dnes.day))
print("Hodina: {:02d}".format(dnes.hour))
print("Minuta: {:02d}".format(dnes.minute))
print("Sekunda: {:02d}".format(dnes.second))
print("Mikrosekunda: {:d}".format(dnes.microsecond))


#Časovač - after (provedení události každých n milisekund)
#okno.after(čas,událost)

from tkinter import *
from datetime import *

hlavni=Tk()

def Vypis():
    print("Proběhl výpis")
    dnes=datetime.now()
    text.delete(1.0,END)
    text.insert(END,"Čas: {:02d}".format(dnes.second))
    hlavni.after(1000,Vypis)

text=Text(hlavni,font="Arial 20")
text.pack()

Vypis()

hlavni.mainloop()







































