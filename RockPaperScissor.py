import random

spelare1 = 0 #Hur många omgångar spelaren har vunnit
Dator = 0 #Hur många omgångar datorn har vunnit

while True:
    rundor = int(input("Skriv in hur många gånger ni vill köra: ")) 

    olika_drag = ["sten", "sax", "påse"]

    poäng = 0 #Poängen, -1 adderas om datorn vinner och +1 adderas om spelaren vinner

    for i in range(rundor):
        drag1 = str(input("Skriv in vilket drag du vill göra: ").lower())

        if drag1 == "sten" or drag1 == "sax" or drag1 == "påse":
            pass
        else:
            print("Det draget finns inte, använd sten, sax eller påse :)")
            continue
    
        drag2 = str(random.choice(olika_drag)) #Datorn randomizar draget
        print("Motståndaren valde:", drag2)

        if drag1 == drag2:            #Jämför dragen för att se vilket som vann 
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

    if poäng > 0:                  #Om poängen är över 0 vann spelaren
        print("Du vann totalen!")
        spelare1 += 1
    elif poäng < 0:                #Om poängen är under 0 vann datorn
        print("Datorn vann totalen!")
        Dator += 1
    else:
        print("Det blev lika i totalen!")
    
    print("Totala poängen blev {}".format(poäng))
    
    if spelare1 > Dator:
        print("Du har vunnit {} omgångar!".format(spelare1))
    elif Dator > spelare1:
        print("Datorn har vunnit {} omgångar!".format(Dator))
    else:
        print("Ni har vunnit lika många omgångar!")
        
    spela_igen = str(input("Vill du spela igen?"))
    
    if spela_igen == "ja":
        pass
    else:                   #Om svaret är ja körs loopen igen annars avslutas den
        break