# Lab 1
# We will enter the first part of this lab:
import math

print('''This program will tell you how many solutions a quadratic has.\n
Before you begin, your equation MUST be in the form ax^2 + bx + c = 0.\n
Enter the coefficients here:''')

# Now we will do the input section

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# We will now do the discriminate
Discrim = int((math.pow(b, 2) - (4)*(a)*(c)))

print("\nThe discriminant of this equation is",Discrim,'.')

# We will now add in part 2 and let the user know how many solutions there are for their given values
if Discrim > 0:
    print("The equation has 2 real solutions.")
if Discrim == 0:
    print("The equation has 1 real solution.")
if Discrim < 0:
    print("The equations has 2 imaginary solutions.")
    
          




