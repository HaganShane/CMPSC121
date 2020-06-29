line = input("Enter a number: ")
Number1 = float(line)

line = input("Enter another number: ")
Number2 = float(line)

# Adding the numbers
NumAdd = Number1 + Number2
print(Number1,"+",Number2,"=",NumAdd)

# Subtracting the numbers
NumSub = Number1 - Number2
print(Number1,"-",Number2,"=",NumSub)

# Multiplying the numbers
NumMult = Number1 * Number2
print(Number1,"*",Number2,"=",NumMult)

# Dividing the numbers
NumDiv = Number1 / Number2
print(Number1,"/",Number2,"=",NumDiv)

# Modulus of numbers
NumMod = Number1 % Number2
print(Number1,"%",Number2,"=",NumMod)

# Sum of numbers
NumSum = NumAdd + NumSub + NumMult + NumDiv + NumMod
print("Sum of numbers:",NumSum)

# Average of numbers
NumAvg = (Number1 + Number2) / 2
print("Average of numbers:",NumAvg)
