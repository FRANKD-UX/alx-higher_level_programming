#!/usr/bin/python3

def print_reverse_alphabet():
    for i in range(122, 96, -1):
        print("{}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end="")
