#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                count += 1
        except (TypeError, ValueError):
            break
    print()
    return count


my_list = [1, 2, 3, 4]
x = len(my_list) + 4
nb_print = safe_print_list_integers(my_list, x)
print("{:d}".format(nb_print))
