import sys
# Asking user for number
num = int(input("Please insert your number: "))

# Checking if provided number is odd or even and printing statement
if (num % 2) == 0:
    print("Your number is odd!")
else:
    print("Your number is even!")

# Asks if You want end a program or type another numbers
no_end = 2
while no_end == 2:
    no_end = int(input("End? Yes = 1 / No = 2"))
    if no_end == 1:
        sys.exit()
    print (input("Please insert your number: "))
    if (num % 2) == 0:
        print("Your number is odd!")
    else:
        print("Your number is even!")






