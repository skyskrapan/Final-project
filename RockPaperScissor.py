import random

sten > sax
sax > påse
påse > sten

olika_drag = ["sten", "sax", "påse"]

drag1 = input()
drag2 = print(random.choice(olika_drag))
if drag1 > drag2:
    print("Du vann")
elif drag1 == drag2:
    print("Det blev lika")
else:
    print("Du förlora")
    
