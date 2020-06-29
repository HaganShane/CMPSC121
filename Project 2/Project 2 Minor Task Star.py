# Project 2
import random

# Tell the user how many people are dining
print("For this simulation, we will say there are five people dining in this party.")
print("Each \"*\" represents 5 minutes past 60 minutes")

# User Input
Parties = int(input("Enter the number of parties: "))
t = 1
s = "*"

Total_Time = 0


while t < Parties + 1:
    # Server Efficiency Constant
    SEC = 2

    # Randomization
    # 1. Random Number
    a = 30
    AandS = int(a * random.random()) + 1

    # 2. Seating Constant
    # We will say the constant here is 3 minutes
    SConst = 3

    # 3. Server Arrival and Ordering Constants
    SAOC = 5

    # 4. Wait for food randomizing
    b = 25
    P1 = int(b * random.random()) + 1
    P2 = int(b * random.random()) + 1
    P3 = int(b * random.random()) + 1
    P4 = int(b * random.random()) + 1
    P5 = int(b * random.random()) + 1
    FinalWait = max(P1, P2, P3, P4, P5)

    # 5. Serving of food

    # 6 Eating Time Randomization
    c = 45
    EatTime = int(c * random.random()) + 1

    # 7 Dessert Ordering Randomization
    x = 1
    y = 5
    Dessert = random.randint(x,y)
    DessertOrder = Dessert * 0.60

    # 8. Wait for Dessert Randomization
    d = 7
    # Add if statement corresponding to if there is anyone who wants dessert    
    if Dessert == 1:
        D1 = int(d * random.random()) + 1
        DMax = D1

    elif Dessert == 2:
        D1 = int(d * random.random()) + 1
        D2 = int(d * random.random()) + 1
        DMax = max(D1,D2)

    elif Dessert == 3:
        D1 = int(d * random.random()) + 1
        D2 = int(d * random.random()) + 1
        D3 = int(d * random.random()) + 1
        DMax = max(D1,D2,D3)

    elif Dessert == 4:
        D1 = int(d * random.random()) + 1
        D2 = int(d * random.random()) + 1
        D3 = int(d * random.random()) + 1
        D4 = int(d * random.random()) + 1
        DMax = max(D1,D2,D3,D4)

    elif Dessert == 5:
        D1 = int(d * random.random()) + 1
        D2 = int(d * random.random()) + 1
        D3 = int(d * random.random()) + 1
        D4 = int(d * random.random()) + 1
        D5 = int(d * random.random()) + 1
        DMax = max(D1,D2,D3,D4,D5)
        

    # 9. Serving of Dessert

    # 10. End of Meal Randomization
    e = 30
    End = int(e * random.random()) + 1


    Total = AandS + SConst + SAOC + FinalWait + SEC + EatTime + DessertOrder + DMax + SEC + End

    Total2 = int(Total)

# Create the output of stars
    Star = (Total2 - 60) % 5
    Remand = 5 - Star
    Total3 = Total2 + Remand
    if Star > 0:
        StarFinal = int((Total3-60) / 5)
    elif Star == 0:
        StarFinal = int((Total2 - 60) / 5)

    OutPut = StarFinal * s

    Total_Time += Total

    print("Trial",t,":",OutPut)
    t += 1

AvgTime = Total_Time / Parties
print("Average dining time among all parties in the simulation:",AvgTime,"minutes")    


