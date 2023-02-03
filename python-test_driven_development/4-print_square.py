#!/usr/bin/python3
""" Print full name """


def print_square(size):
    """ Print full name """
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
