import random
a=random.randint(1,6)
b=random.randint(1,6)
c=random.randint(1,6)
d=random.randint(1,6)
e=random.randint(1,6)
prumer=(a+b+c+d+e)/5
print("Kostka hodila",a,b,c,d,e,"průměr hodů je",prumer)
print("Hrajeme hru kámen, nůžky papír")
print("1) Kámen")
print("2) Nůžky")
print("3) Papír")
v=int(input("Zadej svou volbu: "))
n=random.randint(1,3)
if v==1:
    if n==1:
        print("Volil jsi kámen, počítač také - remíza")
    elif n==2:
        print("Volil jsi kámen, počítač nůžky - vyhráváš")
    else:
        print("Volil jsi kámen, počítač papír - počítač vyhrál")
elif v==2:
    if n==1:
        print("Volil jsi nůžky, počítač kámen - počítač vyhrál")
    elif n==2:
        print("Volil jsi nůžky, počítač také - remíza")
    else:
        print("Volil jsi nůžky, počítač papír - vyhráváš")
elif v==3:
    if n==1:
        print("Volil jsi papír, počítač kámen - vyhráváš")
    elif n==2:
        print("Volil jsi papír, počítač nůžky - počítač vyhrál")
    else:
        print("Volil jsi papír, počítač také - remíza")
else:
    print("ERROR: Musíš zvolit číslo 1-3")
