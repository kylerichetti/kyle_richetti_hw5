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
    pass


#Main Function
def main():
    for i in range(0,3):
        print("Enter your PIN: ")
        pin = input()
        print(pin)
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
