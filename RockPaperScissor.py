import random

rundor = int(input("Skriv in hur många gånger ni vill köra: "))

olika_drag = ["sten", "sax", "påse"]

poäng = 0

for i in range(rundor):
    drag1 = str(input("Skriv in vilket drag du vill göra: ").lower())

    if drag1 == "sten" or drag1 == "sax" or drag1 == "påse":
        pass
    else:
        print("Det draget finns inte, använd sten, sax eller påse :)")
        continue
    
    drag2 = str(random.choice(olika_drag))
    print("Motståndaren valde:", drag2)

    if drag1 == drag2:
        print("Det blev lika!")
    
    elif drag1 == "sten":
        if drag2 == "påse":
            print("Du förlora!")
            poäng -= 1
        else:
            print("Du vann!")
            poäng += 1

    elif drag1 == "påse":
        if drag2 == "sten":
            print("Du vann!")
            poäng += 1
        else:
            print("Du förlora!")
            poäng -= 1

    elif drag1 == "sax":
        if drag2 == "påse":
            print("Du vann!")
            poäng += 1
        else:
            print("Du förlora!")
            poäng -= 1

if poäng > 0:
    print("Du vann totalen!")
elif poäng < 0:
    print("Datorn vann totalen!")
else:
    print("Det blev lika i totalen!")
    
print("Totala poängen blev {}".format(poäng))