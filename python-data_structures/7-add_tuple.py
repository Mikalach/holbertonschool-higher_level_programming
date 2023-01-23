#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    if a_len < 2 or b_len < 2:
        if a_len == 0:
            sheet_a = (0, 0)
        elif a_len == 1:
            sheet_a = (tuple_a[0], 0)
        else:
            sheet_a = tuple_a
        if b_len == 0:
            sheet_b = (0, 0)
        elif b_len == 1:
            sheet_b = (tuple_b[0], 0)
        else:
            sheet_b = tuple_b
        add1 = sheet_a[0] + sheet_b[0]
        add2 = sheet_a[1] + sheet_b[1]
        output = (add1, add2)
        return output
    sheet_a = tuple_a
    sheet_b = tuple_b
    add1 = sheet_a[0] + sheet_b[0]
    add2 = sheet_a[1] + sheet_b[1]
    output = (add1, add2)
    return output
