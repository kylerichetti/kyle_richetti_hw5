#1/user/bin/env python3
import sys

def valid(pin):
    """
    Validate user input
    Arguments:
        pin: the pin to be validated
    Returns:
        True if PIN is valid and correct
        False otherwise
    """
    if len(pin) != 4:
        #Test the length of the pin
        print("Invalid PIN length. Correct format is <####>")
        return(0)
    elif not pin.isdigit():
        #Test to see if the pin contains non-digit characters
        print("Invalid PIN character. Correct format is <####>")
        return(0)
    elif pin == "1234":
        #Test if the pin matches a hard coded "correct" value
        print("Your pin is correct")
        exit(0)
    pass


#Main Function
def main():
    """
    Allows the user to enter their pin up to 3 times
    testing to see if it is valid each time
    """
    for i in range(0,3):
        print("Enter your PIN: ")
        pin = input()
        if valid(pin):
            print("Your PIN is correct")
            exit(0)
        else:
            print("You PIN is incorrect")

    print("You bank card is blocked")
    exit(1)


if __name__ == "__main__":

    main()
    exit(0)
