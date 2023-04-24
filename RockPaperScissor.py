import random

olika_drag = ["sten", "sax", "påse"]
while True:
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
        else:
            print("Du vann!")

    elif drag1 == "påse":
        if drag2 == "sten":
            print("Du vann!")
        else:
            print("Du förlora!")

    elif drag1 == "sax":
        if drag2 == "påse":
            print("Du vann!")
        else:
            print("Du förlora!")
    break