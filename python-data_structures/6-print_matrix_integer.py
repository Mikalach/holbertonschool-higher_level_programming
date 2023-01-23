#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for height in range(len(matrix)):
            for width in range(len(matrix[height])):
                print("{:d}".format(matrix[height][width]), end="")
                if width < len(matrix[height]) - 1:
                    print(" ", end='')
            print("")
