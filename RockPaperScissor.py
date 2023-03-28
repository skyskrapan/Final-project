import random

sten = 1
sax = 2
påse = 3

sten > sax
sax > påse
påse > sten

olika_drag = ["sten", "sax", "påse"]

drag1 = input()
drag2 = str(random.choice(olika_drag))
print(drag2)

if drag1 == påse and drag2 == sten:
    print("Du vann!")
        
else:
    pass

if drag1 > drag2:
    print("Du vann")
          
elif drag1 == drag2:
    print("Det blev lika")
    
else:
    print("Du förlora")
    

