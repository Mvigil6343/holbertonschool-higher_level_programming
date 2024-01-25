#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        alpha = ord(alpha)
        if alpha > 96 and alpha < 123:
            alpha -= 32
        print("{}".format(chr(alpha)), end="")
    print()
