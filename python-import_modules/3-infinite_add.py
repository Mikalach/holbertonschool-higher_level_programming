#!/usr/bin/python3
import sys
if __name__ == "__main__":
    add = sum(int(sys.argv[i]) for i in range(1, len(sys.argv)))
    print("{}".format(add))
