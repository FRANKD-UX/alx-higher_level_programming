#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("Number of argument(s): 0.")
    elif argc == 1:
        print("Number of argument(s): 1 argument:")
    else:
        print("Number of argument(s): {} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
