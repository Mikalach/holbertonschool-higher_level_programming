#!/usr/bin/python3
def print_last_digit(number):

    lastDigit = int(str(abs(number))[-1])
    print(str(lastDigit), end="")
    return lastDigit
