#!/usr/bin/python3
def print_last_digit(number):

    lastDigit = int(str(abs(number))[-1])

    if number < 0:
        print("Last digit of " + str(number) + " is -" +
              str(lastDigit) + " and is less than 6 and not 0")
    elif lastDigit < 6 and lastDigit != 0:
        print("Last digit of " + str(number) + " is " + str(lastDigit) +
              " and is less than 6 and not 0")
    elif lastDigit > 5:
        print("Last digit of " + str(number) + " is " + str(lastDigit) +
              " and is greater than 5")
    else:
        print("Last digit of " + str(number) + " is " + str(lastDigit) +
              " and is 0")
        return lastDigit
