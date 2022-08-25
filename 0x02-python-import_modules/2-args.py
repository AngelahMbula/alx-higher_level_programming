#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("{} argument.".format(n))
    else:
        if n == 1:
            print("{} argument:".format(n))
        else:
            print("{} arguments:".format(n))
        i = 1
        while i <= n:
            print("{} : {:s}".format(i, sys.argv[i]))
            i += 1
