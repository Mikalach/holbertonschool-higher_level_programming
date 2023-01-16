#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = int(str(number)[-1])

if lastDigit > 5:
        print("Last digit of " + str(number) + " is " + str(lastDigit) +
              " and is greater than 5")
elif lastDigit < 6 and lastDigit != 0:
        if  number < 0:
                print("Last digit of " + str(number) + " is -" + str(lastDigit) +
                       " and is less than 6 and not 0")
        else:
                print("Last digit of " + str(number) + " is " + str(lastDigit) +
                      " and is less than 6 and not 0")
else:
        print("Last digit of " + str(number) + " is " + str(lastDigit) +
              " and is 0")
