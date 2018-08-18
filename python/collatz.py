# define user input variable as a blank
user_number = ''

# collatz function, divide even numbers by two, multiply odd numbers by 3 and add 1
def collatz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1
    else:
        return number

# asks user for a number, check to make sure it's a valid integer, otherwise prints an error and asks again
while not user_number:
    try:
        user_number = int(input('Enter Number:' ))
    except ValueError:
        print('Invalid Number, try again')

# loop that calls the collatz function, gets a return and feeds it back to collatz, until the number is 1.
while user_number != 1:
    user_number = collatz(user_number)
    print(user_number)
