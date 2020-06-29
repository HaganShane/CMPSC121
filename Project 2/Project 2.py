# Project 2
import random

# Tell the user how many people are dining
print("For this simulation, we will say there are five people dining in this party.")

# Server Efficiency Constant
SEC = 2

# Randomization
# 1. Random Number
a = 30
AandS = int(a * random.random()) + 1
print("1. Arrival and Seating: Let's say this party is seated",AandS,"minutes after arriving.\n")

# 2. Seating Constant
# We will say the constant here is 3 minutes
SConst = 3
print("2. Seating: It takes",SConst,"minutes for the host to seat this party.\n")

# 3. Server Arrival and Ordering Constants
SAOC = 5
print('''3. Server Arrival and Ordering: Say the \"server efficiency constant\" is 2 minutes i.e. it takes 2 minutes everytime we need to wait for the server to do something.
We wait 2 minutes for the server to arrive. Then, suppose we have 5 people in this party and the time it takes each person to order is
0.60 minutes. Thus, we waited 2 minutes for the server to arrive and 3 minutes for everyone to order, so this step took 5 total minutes.\n''')

# 4. Wait for food randomizing
b = 25
P1 = int(b * random.random()) + 1
P2 = int(b * random.random()) + 1
P3 = int(b * random.random()) + 1
P4 = int(b * random.random()) + 1
P5 = int(b * random.random()) + 1
FinalWait = max(P1, P2, P3, P4, P5)

print('''4. Wait for Food: Suppose it takes''',P1,'''minutes for the first person's meal,''',P2,'''minutes for the second person's meal,''',P3,'''minutes for the third person's meal,''',P4,'''minutes for the fourth person's meal, and''',P5,'''minutes for the fifth person's meal. Thus, it will take''',FinalWait,'''
minutes until the entire party's meal is ready to be served.\n''')

# 5. Serving of food
print("5. Serving of Food: The \"server efficiency constant\" of 2 minutes must be waited until the party gets its food.\n")

# 6 Eating Time Randomization
c = 45
EatTime = int(c * random.random()) + 1
print("6. Eating Time: Suppose it takes this party",EatTime,"minutes to eat their meal.\n")

# 7 Dessert Ordering Randomization
x = 1
y = 5
Dessert = random.randint(x,y)
DessertOrder = Dessert * 0.60
print('''7. Dessert Ordering: Suppose''',Dessert,'''of''',y,'''people in this party want dessert. Thus it will
take each person 0.60 minutes (the constant from above) and a total of''',DessertOrder,'''minutes
to order their desserts.\n''')

# 8. Wait for Dessert Randomization
d = 7
# Add if statement corresponding to if there is anyone who wants dessert    
if Dessert == 1:
    D1 = int(d * random.random()) + 1
    DMax = D1
    print('''8. Wait For Dessert: Since one person ordered dessert, we only wait for their
          dessert to be prepared. We will wait''',DMax,''' minutes''')
elif Dessert == 2:
    D1 = int(d * random.random()) + 1
    D2 = int(d * random.random()) + 1
    DMax = max(D1,D2)
    print('''8. Wait For Dessert: Suppose the first person's dessert takes''',D1,'''minutes to prepare
          and the second person's dessert takes''',D2,'''minutes to prepare. Thus, we wait''',DMax,'''
          minutes for the dessert to arrive.\n''')
elif Dessert == 3:
    D1 = int(d * random.random()) + 1
    D2 = int(d * random.random()) + 1
    D3 = int(d * random.random()) + 1
    DMax = max(D1,D2,D3)
    print('''8. Wait For Dessert: Suppose the first person's dessert takes''',D1,'''minutes to prepare,
          the second person's dessert takes''',D2,'''minutes to prepare, and the third person's
          dessert takes''',D3,'''minutes to prepare. Thus, we wait''',DMax,'''minutes for the dessert to arrive.\n''')
elif Dessert == 4:
    D1 = int(d * random.random()) + 1
    D2 = int(d * random.random()) + 1
    D3 = int(d * random.random()) + 1
    D4 = int(d * random.random()) + 1
    DMax = max(D1,D2,D3,D4)
    print('''8. Wait For Dessert: Suppose the first person's dessert takes''',D1,'''minutes to prepare,
          the second person's dessert takes''',D2,'''minutes to prepare, the third person's
          dessert takes''',D3,'''minutes to prepare, and the fourth person's dessert takes''',D4,'''minutes
          to prepare. Thus, we wait''',DMax,'''minutes for the dessert to arrive.\n''')
elif Dessert == 5:
    D1 = int(d * random.random()) + 1
    D2 = int(d * random.random()) + 1
    D3 = int(d * random.random()) + 1
    D4 = int(d * random.random()) + 1
    D5 = int(d * random.random()) + 1
    DMax = max(D1,D2,D3,D4,D5)
    print('''8. Wait For Dessert: Suppose the first person's dessert takes''',D1,'''minutes to prepare,
          the second person's dessert takes''',D2,'''minutes to prepare, the third person's
          dessert takes''',D3,'''minutes to prepare, the fourth person's dessert takes''',D4,'''minutes
          to prepare, and the fifth person's dessert takes''',D5,'''minutes to prepare.
          Thus, we wait''',DMax,'''minutes for the dessert to arrive.\n''')
    

# 9. Serving of Dessert
print("9. Serving of Dessert: We wait 2 minutes for the dessert to arrive.\n")

# 10. End of Meal Randomization
e = 30
End = int(e * random.random()) + 1
print("10. End of Meal: Suppose this group stays at the table",End,"minutes.\n")


Total = AandS + SConst + SAOC + FinalWait + SEC + EatTime + DessertOrder + DMax + SEC + End
print('''Thus, it took''',AandS,'''+''',SConst,'''+''',SAOC,'''+''',FinalWait,'''+''',SEC,'''+''',EatTime,'''+''',DessertOrder,'''+''',DMax,'''+''',SEC,'''+''',End,'''=''',Total,'''minutes from when
this party arrived until it left.''')

