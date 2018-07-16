print("Hello")
# Asks for name, saves input as variable 'name'
name = input("What is your name? ")
# Prints Hello + saved name variable
print("Hello " + name)

# Asks for users favorite number
number = input("What is your favorite number? ")
# Creates the variable 'triple' which converts the user input for number into an integer rather than a sting using 'int'
triple = int(number) * 3
# Converts 'triple' back toa string to append it to the print function,
# since adding the + operator on an integer attempts to combine strings but add integers
print("Your number multiplied by three is " + str(triple))