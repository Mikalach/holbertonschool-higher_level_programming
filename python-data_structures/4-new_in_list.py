#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new = my_list[:]
        if idx < 0:
            return(new)
        elementNbr = len(my_list) - 1
        if idx > elementNbr:
            return(new)
        else:
            new[idx] = element
            return(new)
